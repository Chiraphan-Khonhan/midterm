#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def callback(scan):
 
    middle_index = len(scan.ranges) // 2
    distance = scan.ranges[middle_index]
    rospy.loginfo("Front distance: %.2f m" % distance)

def laser_subscriber():
    rospy.init_node('laser_subscriber', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    laser_subscriber()

