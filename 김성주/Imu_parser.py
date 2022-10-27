#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion

class ImuParser():
    def __init__(self):
        rospy.init_node('ImuParser', anonymous=False)
        rospy.Subscriber('imu', Imu, self.imu_callback)
        
        
    def imu_callback(self, data):
        quaternion = (data.orientation.x,
                      data.orientation.y,
                      data.orientation.z,
                      data.orientation.w)
        
        euler = euler_from_quaternion(quaternion)
        roll, pitch, yaw = euler
        rospy.loginfo("roll : %f, pitch : %f, yaw : %f", roll, pitch, yaw)

if __name__ == "__main__":
    try:
        ImuParser()
        rospy.spin()
    
    except rospy.ROSInterruptException:
        pass