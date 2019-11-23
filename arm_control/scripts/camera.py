#! /usr/bin/python

import os
import rospy
import rospkg
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

# Instantiate CvBridge
bridge = CvBridge()


class ImageSaver:

    def __init__(self, path):
        self.ImageNumber = 0
        self.ImagePath = path

    def callback(self, msg):
        try:
            # Convert ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError, e:
            print(e)
        else:
            # Save OpenCV2 image as a jpeg
            self.ImageNumber += 1
            filename = self.ImagePath + str(self.ImageNumber) + '.jpg'
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
    # get an instance of RosPack with the default search paths
    rospack = rospkg.RosPack()
    # get the file path for arm_senser package
    pkg_path = rospack.get_path('arm_control')

    # create the folder to store the images
    folder_name = 'images'
    folder_path = pkg_path + '/' + folder_name

    try:
        os.mkdir(folder_path)
    except OSError:
        print("Creation of the directory %s failed" % folder_path)
    else:
        print("Successfully created the directory %s " % folder_path)

    # add an image name to the path
    image_name = 'images_'
    image_path = folder_path + '/' + image_name

    # create image saver
    saver = ImageSaver(image_path)
    # run the saving process
    saver.main()
