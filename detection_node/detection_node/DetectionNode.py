#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
import cv2

from sensor_msgs.msg import Image
from vision_msgs.msg import ObjectHypothesisWithPose, BoundingBox2D
from vision_msgs.msg import Detection2D, Detection2DArray

from ModelWrapper import ModelWrapper

class DetectionNode(Node):
    def __init__(self):
        # Create node
        super().__init__('detection_node')
        # Setup CV bridge
        self.br = CvBridge()

        # Setup model
        model_wrapper = ModelWrapper.ModelWrapper()
        if model_wrapper.load_model('ultralytics/yolov5','yolov5s'):
            self.model = model_wrapper.get_model()
            self.get_logger().info('Model loaded correctly. Nice job!.')
        else:
            self.get_logger().warn('Model not loaded correctly. Please inspect.')

        # Setup subscribers and publishers
        # TODO: change topic to dynamic string
        self.subscriber = self.create_subscription(Image, "/color/image", self.detect_callback,10)

    def detect_callback(self,data):
        self.get_logger().info('Receiving video frame')
        current_frame = self.br.imgmsgs_to_cv2(data)
        cv2.imshow("camera", current_frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    dn = DetectionNode()
    rclpy.spin(dn)
    dn.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


        
