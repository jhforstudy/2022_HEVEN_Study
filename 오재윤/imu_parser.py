#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion

def euler_from_quaternion(x, y, z, w):
    t0 = +2.0 * (w * x * y * z)
    t1 = +1.0 - 2.0 * (x * x * + y * y)
    roll_x = math.degrees(math.atan2(t0, t1))

    t2 = +2.0 * (w * x + y * z)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.degrees(math.asin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.degrees(math.atan2(t3, t4))

    return roll_x, pitch_y, yaw_z

class ImuParser():
    def __init__(self):
        self.roll = 0
        self.pitch = 0
        self.yaw = 0

        rospy.Subscriber("imu", Imu, self.imu_callback)
        rospy.init_node("imu_parser_node", anonymous=False)

    def imu_callback(self, data):
        quar_x = data.orientation.x
        quar_y = data.orientation.y
        quar_z = data.orientation.z
        quar_w = data.orientation.w

        self.roll, self.pitch, self.yaw = euler_from_quaternion(quar_x, quar_y, quar_z, quar_w)
        print("roll : %s, pitch : %s, yaw : %s" %(self.roll, self.pitch, self.yaw))

if __name__ == "__main__":
    try:
        ImuParser()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass