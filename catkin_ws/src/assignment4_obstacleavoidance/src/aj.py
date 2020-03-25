#!/usr/bin/env python
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
#from rospy import Time
import rospy
import numpy as np
import math

# Assignment 4, Obstacle Avoidance, team 7.


def callback(msg):

    # Propertional gain for turning the turtlebot
    Kp = 0.4

    # Proportional gain for moving the bot forward. If this is changed to be larger, the
    # threshold needs to be larger or it will be very close to hitting the wall, and may
    # hit the wall when attempting to turn around.
    Kp_forward = 0.2    # NOTE: if this is changed, need to change threshold

    # Threshold variable for distance from objects, do not change to be too low
    threshold = 0.5

    # Variable to move forward
    throttle = 0

    # Variable to turn
    steer_control = 0

    # Get the scan data for that is to the left, 20 degrees (starting from center at 0)
    forward_scan  = msg.ranges[339:20]

    forward = min(forward_scan)

    # If the forward left value is infinite, then set it to 10
    if forward == float("inf"):
        forward = 10
        
    # Get the scan data for that is to the left, 20 to 90 degrees (starting from center at 0)
    left_scan  = msg.ranges[20:50]

    # Get the scan data for that is to the right, 269 to 339 degrees (starting from center at 0)
    right_scan = msg.ranges[309:339]
    
    # Find the minimum value to get the minimum distance to an object in the left region
    left = min(left_scan)
    
    # Find the minimum value to get the minimum distance to an object in the right region
    right = min(right_scan)


    if forward > left and forward > right :
	throttle = front * Kp_forward
        steer_control = 0
    elif left > forward and left > right :
	steer_control = Kp * (left_wall - right_wall)
	throttle = 0.3
    elif right > forward and right > left :
	steer_control = Kp * (left_wall - right_wall)
	throttle = 0.3

    # Set the variables for the linear and angular movements.
    move.linear.x = throttle
    move.angular.z = steer_control

    pub.publish(move)


move = Twist() # Creates a Twist message type object
rospy.init_node('wall_follower_node',anonymous= True) # Initializes a node
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

sub = rospy.Subscriber("/scan", LaserScan, callback)
                              
rospy.spin()
