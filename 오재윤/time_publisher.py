#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/my_time', String, queue_size=10)
    rospy.init_node('publisher_node', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rostime = "%s" % rospy.get_time()
        rospy.loginfo(rostime)
        pub.publish(rostime)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass