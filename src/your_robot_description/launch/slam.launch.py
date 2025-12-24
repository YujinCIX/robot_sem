from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'odom_frame': 'odom',
            'map_frame': 'map',
            'base_frame': 'base_link',
            'scan_topic': '/scan',
            'minimum_travel_distance': 0.5,
            'minimum_travel_heading': 0.5,
            'scan_buffer_size': 10,
            'map_update_interval': 5.0
        }]
    )

    return LaunchDescription([
        slam_node,
    ])
