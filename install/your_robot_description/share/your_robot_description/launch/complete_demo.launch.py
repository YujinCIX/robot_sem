import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_share = FindPackageShare('your_robot_description').find('your_robot_description')
    launch_dir = os.path.join(pkg_share, 'launch')

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_dir, 'gazebo.launch.py')),
        launch_arguments={}
    )

    rviz_launch = TimerAction(
        period=2.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(launch_dir, 'rviz.launch.py')),
                launch_arguments={}
            )
        ]
    )

    slam_launch = TimerAction(
        period=4.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(launch_dir, 'slam.launch.py')),
                launch_arguments={}
            )
        ]
    )

    nav2_launch = TimerAction(
        period=6.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(launch_dir, 'nav2.launch.py')),
                launch_arguments={}
            )
        ]
    )

    return LaunchDescription([
        gazebo_launch,
        rviz_launch,
        slam_launch,
        nav2_launch,
    ])
