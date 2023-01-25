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
        model_wrapper = ModelWrapper()
        if model_wrapper.load_model('ultralytics/yolov5','yolov5s'):
            self.model = model_wrapper.get_model()
            self.get_logger().info('Model loaded correctly. Nice job!.')
        else:
            self.get_logger().warn('Model not loaded correctly. Please inspect.')

        # Setup subscribers and publishers
        # TODO: change topic to dynamic string
        self.subscriber = self.rospy.Subscriber("/color/image", Image, self.detect_callback)



    def detect_callback(self,data):
        current_frame = self.br.imgmsgs_to_cv2(data)
        


        