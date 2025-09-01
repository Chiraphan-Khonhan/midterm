#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import math
import random

def laser_publisher():
    pub = rospy.Publisher('/scan', LaserScan, queue_size=10)
    rospy.init_node('fake_laser_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        scan = LaserScan()

       
        scan.header.stamp = rospy.Time.now()
        scan.header.frame_id = "base_scan"

     
        scan.angle_min = -math.pi / 2 
        scan.angle_max = math.pi / 2    
        scan.angle_increment = math.radians(1) 

     
        scan.time_increment = 0.0
        scan.scan_time = 0.1

      
        scan.range_min = 0.1
        scan.range_max = 10.0

       
        num_readings = int((scan.angle_max - scan.angle_min) / scan.angle_increment)


        scan.ranges = [random.uniform(0.5, 5.0) for _ in range(num_readings)]
        scan.intensities = [1.0 for _ in range(num_readings)]

       
        pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        laser_publisher()
    except rospy.ROSInterruptException:
        pass

