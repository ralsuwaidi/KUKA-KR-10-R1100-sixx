#!/usr/bin/env python

import rospy
import rostest
import unittest
import numpy as np
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState


class controlTest(unittest.TestCase):
    publisher_working = False
    position = np.array([])

    def move_joint_to(self, pub, value):
        pub.publish(value)

    def joint_name(self, number):
        joint_name = '/kuka_arm/joint' + \
            str(number) + '_position_controller/command'
        return joint_name

    def callback(self, data):
        self.publisher_working = True
        self.position = data.position

    def test_control(self):

        # Check it the joint state publisher is working
        rospy.init_node('integration')
        rospy.Subscriber('/kuka_arm/joint_states', JointState, self.callback)

        rospy.sleep(1)  # wait some time

        self.assertTrue(self.publisher_working,
                        "Joint state publisher is not working! Run the simulation!")

        # Save current robot position
        before_pose = np.array(self.position)

        # Set rate for the publishers
        rate_value = 50  # 50hz
        rate = rospy.Rate(rate_value)
        # Create lists for joints and publishers
        joints = []
        pub = []
        joints_number = 6
        for i in range(joints_number):
            joints.append(self.joint_name(i+1))
            pub.append(rospy.Publisher(joints[i], Float64, queue_size=10))

        # Give a command for the robot to move to the initial state
        desired_pose = np.array(np.deg2rad([0, 0, 0, 0, 0, 0]))
        time = 200
        speed = 100
        for j in range(time):
            for i in range(joints_number):
                try:
                    self.move_joint_to(pub[i], speed*desired_pose[i])
                except rospy.ROSInterruptException:
                    pass
            rate.sleep()

        # Save robot position after the command
        after_pose = np.array(self.position)

        # Compare robot position before and after the command
        flag = np.array_equal(before_pose, after_pose)
        self.assertEqual(flag, False, "Robot is not moveable!")

        # Compare desired robot position and position after the command
        delta = 0.1
        for i in range(joints_number):
            msg = joints[i] + ' did not move to the desired position!'
            self.assertAlmostEqual(
                desired_pose[i], after_pose[i], msg=msg, delta=delta)


if __name__ == '__main__':
    rostest.rosrun('arm_control', 'integration', controlTest, sysargs=None)
