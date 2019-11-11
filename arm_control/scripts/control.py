#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math
 
def talker():
    pub = rospy.Publisher('/kuka_arm/joint2_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate_value = 50 # 50hz
    rate = rospy.Rate(rate_value)
    while not rospy.is_shutdown():
        i = rospy.get_time()
        position = math.sin(i/rate_value)*1.5 - 2
        #rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
