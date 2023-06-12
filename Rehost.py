import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

class MyNode(Node):

    def __init__(self):
        super().__init__('host')
        self.publisher = self.create_publisher(Twist, 'To_khedas', 10)
        self.subscription1 = self.create_subscription(
            Twist,
            'cmd',
            self.listener_callback_twist,
            10)
        self.subscription1  # prevent unused variable warning
        self.subscription2 = self.create_subscription(
            Vector3,
            'From_khadas',
            self.listener_callback_float,
            10)
        self.subscription2  # prevent unused variable warning

        self.subscription2 = self.create_subscription(
            Vector3,
            'From_khadas',
            self.listener_callback_float,
            10)
        self.subscription2  # prevent unused variable warning

    def listener_callback_twist(self, msg):
        self.publisher.publish(msg)

        self.get_logger().info('Received twist message: "%s"' % msg)

    def listener_callback_float(self, msg):
        print("aaaaaaaaaaaaaaaaA",msg)
        #self.get_logger().info('Received float message: "%s"' % msg.data)

    def send_twist(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()