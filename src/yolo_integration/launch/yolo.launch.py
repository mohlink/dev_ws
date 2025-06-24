import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='yolo_integration',
            executable='yolo_node',
            output='screen',
        )
    ])
