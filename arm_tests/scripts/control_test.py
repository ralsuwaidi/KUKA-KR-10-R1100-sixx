#!/usr/bin/env python

import unittest
import rospy
from std_msgs.msg import Float64
from time import sleep
import rostest

class publishermsg_test(unittest.TestCase):
    publisher_working = False

    def callback(self, data):
        self.publisher_working = True
	print(data)
    
    def test_publisher(self):
        rospy.init_node('publisher_test')
        rospy.Subscriber('/kuka_arm/joint3_position_controller/command', Float64, self.callback)

        counter = 0
        while not rospy.is_shutdown() and counter < 2 and (not self.publisher_working):
            sleep(1)
            counter +=1

        self.assertTrue(self.publisher_working)


if __name__ == '__main__':
    rostest.rosrun('arm_tests', 'publisher_test', publishermsg_test, sysargs=None)
