import rclpy
import time


from geometry_msgs.msg import Twist

import sys, select, termios, tty

settings = termios.tcgetattr(sys.stdin)


def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def main(args=None):	

    rclpy.init(args=args)
    node = rclpy.create_node('cmd')
        
    pub = node.create_publisher(Twist, 'cmd', 3)

    speed=0
    c=0

    while(1):
        key = getKey()
        if key == "w":
            print("전진")
            c = 0
            if speed == 360:
                speed = 360
            else:
                speed += 10
            print("속도: ", speed)

        if key == "s":
            print("후진")
            c = 0
            if speed == -360:
                speed = 360
            else:
                speed -= 10
            print("속도: ", speed)

        if key == "a":
            print("좌회전")
            speed=0.0
            c=2.0

        if key == "d":
            print("우회전")
            speed=0.0
            c=1.0

        if key == "q":
            print("멈춤")
            speed = 0.0
            c = 0.0

        if key == "e":
            print("나가기")
            speed = 0.0
            c = 0.0
            break

        twist = Twist()
        speed=float(speed)
        twist.linear.x = speed; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = float(c)
        pub.publish(twist)


        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

main()