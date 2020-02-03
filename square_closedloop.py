#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt

class turtlebot():

    def __init__(self):
        #Create a node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    #Callback function which is called when a new message of type Pose is received by the subscriber
    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def move2goal(self):
	#Moves the turtle to the goal
	position = [[0,0], [0,0], [0,0], [0,0], [0,0]]
        goal_pose = Pose()

	for m in range (0,5):
	    X_position = input("Set your X goal: ")
	    Y_position = input("Set your Y goal: ")
	    position[m][0] = X_position
	    position[m][1] = Y_position

        	
        goal_tolerance = input("Set your tolerance:")
        vel_msg = Twist()


	for n in range (0,5):
      	    
     	    angular_speed = abs((atan2(position[n][1] - self.pose.y, position[n][0] - self.pose.x) - self.pose.theta))
            while  angular_speed >= 0.01:
            
	    #angular velocity in the z-axis:
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 2 * angular_speed

            #Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()
	    
	    delta_distance = sqrt(pow((position[n][0] - self.pose.x), 2) + pow((position[n][1] - self.pose.y), 2))

	    while  delta_distance >= goal_tolerance:
            #Proportional Controller
            #linear velocity in the x-axis:
                vel_msg.linear.x = 2 * delta_distance
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
	        vel_msg.angular.z = 0

 	        self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()

          
        #Stopping our robot after the movement is over
            vel_msg.linear.x = 0
            vel_msg.angular.z =0
            self.velocity_publisher.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.move2goal()

    except rospy.ROSInterruptException: pass
