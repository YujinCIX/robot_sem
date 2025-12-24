import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    nav2_bringup_dir = FindPackageShare('nav2_bringup').find('nav2_bringup')
    nav2_launch = os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
    
    pkg_share = FindPackageShare('your_robot_description').find('your_robot_description')
    config_dir = os.path.join(pkg_share, 'config')
    
    nav2_launch_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch),
        launch_arguments={
            'use_sim_time': 'True',
            'params_file': os.path.join(config_dir, 'nav2_params.yaml'),
            'autostart': 'True'
        }
    )

    return LaunchDescription([
        nav2_launch_description,
    ])
