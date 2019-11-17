#!/usr/bin/env python

import rospy
import rostest
import unittest
import numpy as np
from time import sleep
from sensor_msgs.msg import JointState




class moveableTest(unittest.TestCase):
    publisher_working = False
    joints = np.array([])

    def callback(self, data):
        self.publisher_working = True
        self.joints = data.position

    def test_moveable(self):
        rospy.init_node('publisher_test')
        rospy.Subscriber('/kuka_arm/joint_states', JointState, self.callback)

        sleep(1)

        # check if the joint_state_publisher is working
        self.assertTrue(self.publisher_working, "Joint state publisher is not working!")
        
        # robot initial position
        initial_pose = np.array(np.deg2rad([0, -90, 0, 0, 0, 0]))
        # robot current position
        current_pose = np.array(self.joints)

        # compare robot current position with the initial one
        flag = np.array_equal(current_pose, initial_pose)
        
        # if they are different - robot is moveable
        self.assertEqual(flag, False, "Robot is not moveable!")


        


if __name__ == '__main__':
    rostest.rosrun('arm_tests', 'publisher_test', moveableTest, sysargs=None)