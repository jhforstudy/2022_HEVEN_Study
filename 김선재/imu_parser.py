#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
import math
 
def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
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
     
        return math.degrees(roll_x), math.degrees(pitch_y), math.degrees(yaw_z) # in radians

class ImuParser():
    def __init__(self):
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        rospy.Subscriber("imu", Imu, self.imu_callback)
        rospy.init_node("imu_parser_node", anonymous=False)


    def imu_callback(self, data):
        x = data.orientation.x
        y = data.orientation.y
        z = data.orientation.z
        w = data.orientation.w

        self.roll, self.pitch, self.yaw = euler_from_quaternion(x, y, z, w)

        print(f"roll : {self.roll}, pitch : {self.pitch}, yaw : {self.yaw}")

if __name__ == "__main__":
    try:
        ImuParser()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass    
