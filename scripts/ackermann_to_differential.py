#!/usr/bin/python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from autoware_control_msgs.msg import Control

import numpy as np

class Converter(Node):
    def __init__(self, l=2.79, t=1.64):
        super().__init__('waypoint_gen')
        
        # Publishers
        self.differential_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Subscribers
        self.ackermann_sub = self.create_subscription(
            Control,
            '/control/command/control_cmd',
            self.ackermann_to_differential_twist_msg,
            10)
        
        # Wheel Tread
        self.t = t
        
        # Wheelbase
        self.l = l
        
    def ackermann_to_differential_twist_msg(self, data: Control):
        v = data.longitudinal.velocity
        delta = data.lateral.steering_tire_angle
            
        cmd_vel = Twist()
        
        # Wheel velocities
        vl = v - (self.t*delta)/2
        vr = v + (self.t*delta)/2
        
        # Angular velocities of wheels
        wl = vl/self.r
        wr = vr/self.r
        
        # Twist Linear x
        V = self.r*(wl+wr)/2
        
        # Twist Angular z
        W = self.r*(wr-wl)/self.t
        
        cmd_vel.linear.x  = V
        cmd_vel.angular.z = W
            
        self.differential_pub.publish(cmd_vel)
            
            
            

            
            
            
            
    

def main(args=None):
    rclpy.init(args=args)
    
    converter = Converter()

    rclpy.spin(converter)

    converter.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
