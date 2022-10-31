#!/usr/bin/env python3
# license removed for brevity

import rospy
from std_msgs.msg import String
 
def talker():
     pub = rospy.Publisher('/my_time', String, queue_size=10)
     rospy.init_node('talker_node', anonymous=False)
     rate = rospy.Rate(10) # 10hz
     while not rospy.is_shutdown():
           pre_time = "%s" % rospy.get_time()
           rospy.loginfo("Publishing topic is %s" %pre_time)
           pub.publish(pre_time)
           rate.sleep()
   
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass