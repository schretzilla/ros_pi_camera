#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge, CvBridgeError

from picamera.array import PiRGBArray
from picamera import PiCamera
import time

def talker():
    #the name of this node
    rospy.init_node('VideoPublisher', anonymous=True)

    #the topic we are publishing image data to
    VideoRaw = rospy.Publisher('VideoRaw', Image, queue_size=10)

    camera = PiCamera()
    camera.resolution = (640, 360)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 360))

    time.sleep(0.1)

    rate = rospy.Rate(10) # 10hz sleep

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array

        #publish the Canny Edge Image and the original Image
        try:
            msg_frame = CvBridge().cv2_to_imgmsg(image, "bgr8")
            VideoRaw.publish(msg_frame)
        except CvBridgeError as e:
            print(e)

        rawCapture.truncate(0)
        rate.sleep()

        if(rospy.is_shutdown()):
           break

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
