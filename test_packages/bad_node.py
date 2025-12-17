import rclpy
# SYNTAX ERROR: Missing colon in class definition
class BadArm(Node)
    def __init__(self):
        super().__init__('bad_arm')
        # SAFETY ERROR: Joint value 5.5 exceeds 3.14 rad limit
        self.joints = [5.5, 0.0, 0.0, 0.0, 0.0, 0.0]

def main() # SYNTAX ERROR: Missing colon
    rclpy.init()
