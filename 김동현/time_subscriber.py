#!usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard, %s" % data.data)

def subscriber():

    sub = rospy.Subscriber("my_time", String, callback)
    rospy.init_node("Subscriber_node", anonymous=False)

    rospy.spin()

if __name__ =="__main__":
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass