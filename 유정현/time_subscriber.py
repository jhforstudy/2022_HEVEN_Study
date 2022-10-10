#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard, %s" % data.data)

def subscriber():
    rospy.init_node("subscriber_node", anonymous=False)
    rospy.Subscriber("my_time", String, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass