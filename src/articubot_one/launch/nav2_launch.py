from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            output='screen',
            parameters=[
                {'use_sim_time': False},
                {'autostart': True},
                {'params_file': '/path_to_your_nav2_params.yaml'},
                {'map': '/path_to_your_map.yaml'}
            ]
        ),
    ])
