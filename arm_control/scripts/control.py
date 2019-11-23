#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import numpy as np


def move_joint(pub, speed, upper_limit, lower_limit):
    i = rospy.get_time()
    diff = (upper_limit - lower_limit)/2
    offset = upper_limit - diff
    position = np.sin(i/rate_value*speed)*diff + offset
    # rospy.loginfo(position)
    pub.publish(position)


def joint_name(number):
    joint_name = '/kuka_arm/joint' + \
        str(number) + '_position_controller/command'
    return joint_name


if __name__ == '__main__':

    speed = 100
    upper_limit = np.pi
    lower_limit = -np.pi

    joints = []
    pub = []
    joints_number = 6
    for i in range(joints_number):
        joints.append(joint_name(i+1))
        pub.append(rospy.Publisher(joints[i], Float64, queue_size=10))

    rospy.init_node('joints_talker', anonymous=True)
    rate_value = 50  # 50hz
    rate = rospy.Rate(rate_value)

    while not rospy.is_shutdown():
        for i in range(joints_number):
            try:
                move_joint(pub[i], speed, upper_limit, lower_limit)
            except rospy.ROSInterruptException:
                pass
        rate.sleep()
