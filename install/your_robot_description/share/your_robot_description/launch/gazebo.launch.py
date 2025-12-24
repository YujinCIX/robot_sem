import os
import xacro
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_share = FindPackageShare('your_robot_description').find('your_robot_description')
    config_dir = os.path.join(pkg_share, 'config')
    xacro_file = os.path.join(pkg_share, 'urdf', 'robot.urdf.xacro')
    world_file = os.path.join(pkg_share, 'worlds', 'corridor_world.world')

    robot_description_config = xacro.process_file(xacro_file)
    robot_description = {'robot_description': robot_description_config.toxml()}

    gz_server = ExecuteProcess(
        cmd=['gz', 'sim', '-s', '-v', '4', world_file],
        output='screen'
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description, {'use_sim_time': True}]
    )

    spawn_robot = TimerAction(
        period=3.0,
        actions=[
            Node(
                package='ros_gz_sim',
                executable='create',
                arguments=[
                    '-name', 'mobile_robot_with_arm',
                    '-topic', 'robot_description',
                    '-x', '0.0', '-y', '0.0', '-z', '0.5'
                ],
                output='screen'
            )
        ]
    )

    controller_manager = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='controller_manager',
                executable='ros2_control_node',
                parameters=[robot_description, 
                           {'use_sim_time': True},
                           os.path.join(config_dir, 'controller_manager.yaml')],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        gz_server,
        robot_state_publisher,
        spawn_robot,
        controller_manager,
    ])
