import rclpy
import serial

from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

class serial_node(Node):

    def __init__(self,port_name):
        super().__init__('khadas')

        # Subscriber init
        self.subscription = self.create_subscription(
            Twist,
            'To_khedas',
            self.listener_callback,
            10)
        
        self.subscription  # prevent unused variable warning

        # Init Serial Communication
        self.Serial_ = serial.Serial(
            port=port_name,
            baudrate=115200
        )

        # Publisher init
        self.publisher_ = self.create_publisher(Vector3, 'From_khadas', 10)

        self.i = 0

    def listener_callback(self, msg):
        # Pyserial TX (Arudino -> ROS2)
        self.i +=0.3
        robot = Twist()
        enco=Vector3()

        robot.linear.x=msg.linear.x
        robot.angular.z=msg.angular.z

        self.serial_write(robot.linear.x,robot.angular.z)
        
        data=self.serial_read()
        print(data)
        if data!= -1:
            enco.x=float(data[0])
            enco.y=float(data[1])
            print(2)
            self.publisher_.publish(enco)
        else:
            print("err")
    
    def serial_write(self,data1,data2):
        
        datafame = '$'+str(data1)+','+str(data2)
        print(datafame)
        self.Serial_.write(datafame.encode())
    
    def serial_read(self):
        response = self.Serial_.readline()
        data = response[:len(response)-2].decode('utf-8')
        print(data)
        data = data.split(',')
        return data
        

def main(args=None):
    rclpy.init(args=args)

    Test_node = serial_node("/dev/ttyUSB0")

    rclpy.spin(Test_node)

    Test_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()