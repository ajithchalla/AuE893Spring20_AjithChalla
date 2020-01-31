#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
      
    
    #Receiveing the user's input
    print("Let's move your robot")
    speed = input("Input your speed:")
    distance = input("Type your distance:")
    
    pi = 3.1415926535897

    req_angle = 90*2*pi/360
    angular_speed = 90*2*pi/360
       
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    for i in range(0,4):
	t0 = float(rospy.Time.now().to_sec())
	current_distance = 0
	
	while(current_distance < distance):
	    vel_msg.linear.x =speed
	    velocity_publisher.publish(vel_msg)
	    t1=float(rospy.Time.now().to_sec())
   	    current_distance= speed*(t1-t0)
	
	vel_msg.linear.x = 0	
	velocity_publisher.publish(vel_msg)
        vel_msg.angular.z = 0.2	
	t0r = float(rospy.Time.now().to_sec())
	current_angle = 0

	while(current_angle<=req_angle):
	    velocity_publisher.publish(vel_msg)
	    t1r=float(rospy.Time.now().to_sec())
	    current_angle = 0.2*(t1r-t0r)

	vel_msg.angular.z = 0 
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
