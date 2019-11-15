#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from gazebo_msgs.msg import LinkStates

def callbackGazebo(data):
    print(data.pose[7], type(data.pose[7]))

def callback(data):
    #rospy.loginfo(data.process_value)
    print(data.position)
    
def listener():

    rospy.init_node('joint_state_sub', anonymous=True)

    rospy.Subscriber("/kuka_arm/joint_states", JointState, callback)

    rospy.Subscriber("/gazebo/link_states", LinkStates, callbackGazebo)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
