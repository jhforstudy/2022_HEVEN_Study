#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('publisher_node', anonymous=False)
    pub = rospy.Publisher('my_time', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        now_time = rospy.get_time()
        rospy.loginfo("%s" %now_time)
        pub.publish("%s" %now_time)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass