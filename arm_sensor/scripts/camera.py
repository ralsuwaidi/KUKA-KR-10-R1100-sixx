#! /usr/bin/python

import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

# Instantiate CvBridge
bridge = CvBridge()


import os
path = os.path.dirname(__file__)
os.chdir(path)

class ImageSaver:

	def __init__(self):
		self.ImageNumber = 0
		self.path = os.getcwd()

	def callback(self, msg):
		rospy.loginfo(msg.header)
		try:
			# Convert your ROS Image message to OpenCV2
			cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
		except CvBridgeError, e:
			print(e)
		else:
			# Save your OpenCV2 image as a jpeg
			self.ImageNumber += 1
			filename = self.path + '/images/camera_image_' + str(self.ImageNumber) + '.jpg'
			print filename			
			cv2.imwrite(filename, cv2_img)

	def main(self):
		rospy.init_node('camera_image_saver')
		# Define your image topic
		image_topic = "/kuka_arm/camera/image_raw"
		# Set up your subscriber and define its callback
		rospy.Subscriber(image_topic, Image, self.callback)
		# Spin until ctrl + c
		rospy.spin()

if __name__ == '__main__':
	ImageSaver().main()

