import rclpy
from rclpy.node import Node

class SimpleArm(Node):
    def __init__(self):
        super().__init__('simple_arm')
        # Safe joint values (under 3.14 rad)
        self.joints = [1.5, -1.0, 0.0, 0.5, 1.2, 0.0]
        self.get_logger().info("Arm initialized safely.")

def main():
    rclpy.init()
    node = SimpleArm()
    rclpy.spin_once(node)
