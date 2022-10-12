#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard : %s", data.data)
    
def listener():

    rospy.init_node('subscriber_node', anonymous=False)

    rospy.Subscriber("my_time", String, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
