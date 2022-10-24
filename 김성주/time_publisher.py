#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def time_pub():
    pub = rospy.Publisher('/my_time', String, queue_size=10)
    rospy.init_node('time_pub', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        cur_time = "%s" % rospy.get_time()
        pub.publish(cur_time)
        rospy.loginfo("Published time : %s", cur_time)
        rate.sleep()

if __name__ == '__main__':
    try:
        time_pub()
    except rospy.ROSInterruptException:
        pass