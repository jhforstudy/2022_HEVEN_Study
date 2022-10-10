#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node("publisher_node", anonymous=False)
    pub = rospy.Publisher("my_time", String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        now_time = rospy.get_time()
        pub.publish("%s" % now_time)
        rospy.loginfo("%s" % now_time)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass