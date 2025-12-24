import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from moveit_configs_utils import MoveItConfigsBuilder
from launch_ros.actions import RvizNode

def generate_launch_description():
    pkg_share = FindPackageShare('your_robot_description').find('your_robot_description')
    config_dir = os.path.join(pkg_share, 'config')
    xacro_file = os.path.join(pkg_share, 'urdf', 'robot.urdf.xacro')
    
    moveit_config = MoveItConfigsBuilder(
        robot_name='mobile_robot_with_arm',
        package_name='your_robot_description',
        moveit_configs_package_name='your_robot_description'
    ).to_dict()

    move_group = Node(
        package='moveit_ros_move_group',
        executable='move_group',
        output='screen',
        parameters=[
            moveit_config,
            {'use_sim_time': True},
            os.path.join(config_dir, 'moveit_controllers.yaml')
        ]
    )

    rviz_node = RvizNode(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', os.path.join(pkg_share, 'rviz', 'moveit_config.rviz')],
        parameters=[moveit_config]
    )

    return LaunchDescription([
        move_group,
        rviz_node,
    ])
