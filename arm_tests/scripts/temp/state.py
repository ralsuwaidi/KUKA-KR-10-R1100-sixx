#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState

def callback(data):
    #rospy.loginfo(data.process_value)
    print(data.process_value, data.error)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('joint_state_sub', anonymous=True)

    rospy.Subscriber("/kuka_arm/joint1_position_controller/state", JointControllerState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
