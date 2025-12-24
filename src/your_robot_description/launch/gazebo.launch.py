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

    gz_client = TimerAction(
        period=2.0,
        actions=[
            ExecuteProcess(
                cmd=['gz', 'sim', '-g'],
                output='screen'
            )
        ]
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
                    '-x', '0.0',
                    '-y', '0.0',
                    '-z', '0.5'
                ],
                output='screen'
            )
        ]
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description, {'use_sim_time': True}]
    )

    controller_manager = TimerAction(
        period=4.0,
        actions=[
            Node(
                package='controller_manager',
                executable='ros2_control_node',
                parameters=[
                    {'use_sim_time': True},
                    os.path.join(config_dir, 'controller_manager.yaml')
                ],
                output='screen'
            )
        ]
    )

    load_joint_state_broadcaster = TimerAction(
        period=5.0,
        actions=[
            ExecuteProcess(
                cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'joint_state_broadcaster'],
                output='screen'
            )
        ]
    )

    load_diff_drive = TimerAction(
        period=6.0,
        actions=[
            ExecuteProcess(
                cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'diff_drive_controller'],
                output='screen'
            )
        ]
    )

    load_arm_controller = TimerAction(
        period=7.0,
        actions=[
            ExecuteProcess(
                cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'arm_controller'],
                output='screen'
            )
        ]
    )

    return LaunchDescription([
        gz_server,
        gz_client,
        robot_state_publisher,
        spawn_robot,
        controller_manager,
        load_joint_state_broadcaster,
        load_diff_drive,
        load_arm_controller,
    ])
