#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg          import Pose
from std_srvs.srv           import Empty


def circle(linear_vel, angular_vel):
    rospy.init_node('circle_turtle', anonymous=True)
    publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
    

    rate = rospy.Rate(10)                   # 10hz
    vel_msg = Twist()

    while not rospy.is_shutdown():

	vel_msg.linear.x = linear_vel
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = angular_vel

        
	publisher.publish(vel_msg)
        #rate.sleep(10)
        

if __name__ == '__main__':
    try:
        circle(float(1.5), float(1.5))
    except rospy.ROSInterruptException:
        pass


