import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO

class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.subscription = self.create_subscription(
            CompressedImage,
            '/image_raw/compressed',
            #'/camera/image_raw/compressed',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(CompressedImage, '/yolo_image/compressed', 10)
        self.br = CvBridge()
        self.model = YOLO("yolov8n.pt")  # Charger le modèle YOLOv8 pré-entraîné

    def listener_callback(self, data):
        current_frame = self.br.compressed_imgmsg_to_cv2(data)
        results = self.model(current_frame, conf=0.6)  # Définir le seuil de confiance
        results_img = results[0].plot()  # Utiliser .plot() pour obtenir l'image avec les annotations
        output_msg = self.br.cv2_to_compressed_imgmsg(results_img)
        self.publisher_.publish(output_msg)
        cv2.imshow('Video Detection', results_img)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    yolo_node = YoloNode()
    rclpy.spin(yolo_node)
    yolo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
