#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
import math
 
def euler_from_quaternion(x, y, z, w):
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
    
        return roll_x, pitch_y, yaw_z 


class ImuParser():
    def __init__(self):
        self.roll=None
        self.pitch=None
        self.yaw=None
        rospy.Subscriber('imu', Imu, self.imu_callback)
        rospy.init_node('imu_parser_node', anonymous=False)

    def imu_callback(self, data):
        self.roll, self.pitch, self.yaw = euler_from_quaternion(data.orientation.x, data.orientation.y, 
        data.orientation.z, data.orientation.w)
        print("roll : {0}, pitch : {1}, yaw : {2}".format(self.roll, self.pitch, self.yaw))


if __name__=="__main__":
    try:
        ImuParser()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass