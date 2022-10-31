#!/usr/bin/env python3
# license removed for brevity

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Subscribing topic is %s" %data.data)
 
def listener():
    rospy.init_node('listener_node', anonymous=False)
    rospy.Subscriber("/my_time", String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass