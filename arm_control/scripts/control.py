#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math
 
def move_joint(joint_name, speed, upper_limit, lower_limit):
    pub = rospy.Publisher(joint_name, Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate_value = 50 # 50hz
    rate = rospy.Rate(rate_value)
    if not rospy.is_shutdown():
        i = rospy.get_time()
        diff = (upper_limit - lower_limit)/2
        offset = upper_limit - diff
        position = math.sin(i/rate_value*speed)*diff + offset
        #rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def joint_name(number):
    joint_name = '/kuka_arm/joint' + str(number) +'_position_controller/command'
    return joint_name
 
if __name__ == '__main__':

    speed = 100

    while 1:
        joint1 = joint_name(1)   
        move_joint(joint1, speed, math.pi, -math.pi)
        
        joint2 = joint_name(2)
        move_joint(joint2, speed, math.pi, -math.pi)

        joint3 = joint_name(3)
        move_joint(joint3, speed, math.pi, -math.pi)

        joint4 = joint_name(4)
        move_joint(joint4, speed, math.pi, -math.pi)

        joint5 = joint_name(5)
        move_joint(joint5, speed, math.pi, -math.pi)

        joint6 = joint_name(6)
        move_joint(joint6, speed, math.pi, -math.pi)

        if rospy.ROSInterruptException:
            pass
