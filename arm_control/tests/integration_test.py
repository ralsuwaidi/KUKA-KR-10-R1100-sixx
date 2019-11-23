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
        self.position = data.position

    def test_control(self):

        rospy.init_node('integration')
        rospy.Subscriber('/kuka_arm/joint_states', JointState, self.callback)

        # Set desired position and precision
        decimal = 1
        desired_pose = np.array(np.deg2rad([0, 0, 0, 0, 0, 0]))
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

        rospy.sleep(1)  # wait some time

        # Save current robot position
        initial_pose = np.array(self.position)

        # Make sure that initial and desired position are not the same
        np.testing.assert_raises(AssertionError, np.testing.assert_array_almost_equal,
                                 desired_pose, initial_pose, decimal, 'Joints have the same initial and desired position!')

        # Give a command for the robot to move to the initial state
        time = 200
        for j in range(time):
            for i in range(joints_number):
                try:
                    self.move_joint_to(pub[i], desired_pose[i])
                except rospy.ROSInterruptException:
                    pass
            rate.sleep()

        # Save robot position after the command
        final_pose = np.array(self.position)

        # Compare initial and final robot position
        np.testing.assert_raises(AssertionError, np.testing.assert_array_almost_equal,
                                 initial_pose, final_pose, decimal, 'Joints have the same initial and desired position!')

        # Compare desired robot position and position after the command
        np.testing.assert_array_almost_equal(
            desired_pose, final_pose, decimal, 'Robot did not move to the desired position!')


if __name__ == '__main__':
    rostest.rosrun('arm_control', 'integration', controlTest, sysargs=None)
