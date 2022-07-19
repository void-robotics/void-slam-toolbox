import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    pkg_ros_ign_gazebo = get_package_share_directory('ros_ign_gazebo')
    pkg_dolly_ignition = get_package_share_directory('dolly_ignition')
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_ign_gazebo, 'launch', 'ign_gazebo.launch.py'),
        ),
    )

    # Spawn dolly
    spawn = Node(package='ros_ign_gazebo', executable='create',
                 arguments=[
                    '-name', 'dolly',
                    '-x', '6.0',
                    '-z', '0.46',
                    '-Y', '2.57',
                    '-file', os.path.join(pkg_dolly_ignition, 'models', 'dolly_ignition',
                                          'model.sdf')],
                 output='screen')    


    # RViz
    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_dolly_ignition, 'rviz', 'dolly_ignition.rviz')],
        condition=IfCondition(LaunchConfiguration('rviz'))
        )    

    # Bridge
    bridge = Node(
        package='ros_ign_bridge',
        executable='parameter_bridge',
        arguments=['/dolly/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist',
                   '/scan@sensor_msgs/msg/LaserScan@ignition.msgs.LaserScan',
                   '/dolly/odometry@nav_msgs/msg/Odometry]ignition.msgs.Odometry',
                   '/model/dolly/tf@tf2_msgs/msg/TFMessage[ignition.msgs.Pose_V',
                   '/world/station/model/dolly/joint_state@sensor_msgs/msg/JointState@ignition.msgs.Model',
                   '/clock@rosgraph_msgs/msg/Clock@ignition.msgs.Clock'],
        output='screen'
    )


    scan_tf_map = Node(package='tf2_ros', executable='static_transform_publisher',
                arguments = [
                    '0', '0', '0', '0', '0', '0',
                    'base_footprint',
                    'map'
            ])  
    # clock_bridge = Node(package='ros_ign_bridge', executable='parameter_bridge',
    #         output='screen',
    #         arguments=['/clock' + '@rosgraph_msgs/msg/Clock' + '[ignition.msgs.Clock'],
    #         condition=IfCondition(use_sim_time)
    #         )    


    # state_publisher = Node(package='robot_state_publisher', executable='robot_state_publisher',
    #             output='screen',
    #             parameters = [
    #                 {'ignore_timestamp': False},
    #                                     {'use_sim_time': use_sim_time},
    #                 {'use_tf_static': True},
    #                 {'robot_description': open(urdf_path).read()}],
    #             arguments = [urdf_path])

        # '/world/default/model/dolly/joint_state@sensor_msgs/msg/JointState[ignition.msgs.Model'
    #     # remappings=['dolly/tf','/tf']

    #         # joint state bridge 
    # joint_state_bridge = Node(package='ros_ign_bridge', executable='parameter_bridge',
    #         namespace = namespace,
    #         name = 'joint_state_bridge',
    #         output='screen',
    #         parameters=[{
    #             'use_sim_time': use_sim_time
    #         }],
    #         arguments = [
    #             '/world/station/model/dolly/joint_state@sensor_msgs/msg/JointState[ignition.msgs.Model'
    #         ],
    #         remappings = [
    #             ('/world/default/model/igt_one/joint_state', '/joint_states')
    #         ])


    # tf = Node(
    #         package="tf2_ros",
    #         executable="static_transform_publisher",
    #         output="screen" ,
    #         arguments=["0", "0", "0", "0", "0", "0","/dolly/odometry", "dolly/chassis/sensor_ray"]
    #         # dolly/chassis/sensor_ray
    #     )

    # state_publisher = Node(package='robot_state_publisher', executable='robot_state_publisher',
    #             output='screen',
    #             parameters = [
    #                 {'ignore_timestamp': False},
    #                                     {'use_sim_time': use_sim_time},
    #                 {'use_tf_static': True},
    #                 {'robot_description': open(urdf_path).read()}],
                # arguments = [urdf_path])
    # lidar_tf = Node(package='tf2_ros', executable='static_transform_publisher',
    #             arguments = [
    #                 '0', '0', '0', '0', '0', '0',
    #                 '/scan',
    #                 'dolly/chassis/sensor_ray'
    #         ])


    # map_tf = Node(package='tf2_ros', executable='static_transform_publisher',
    #             arguments = [
    #                 '0', '0', '0', '0', '0', '0',
    #                 'map',
    #                 '/dolly/odometry'
    #         ])

    # odom_tf = Node(package='tf2_ros', executable='static_transform_publisher',
    #             arguments = [
    #                 '0', '0', '0', '0', '0', '0',
    #                 '/dolly/odometry',
    #                 'dolly/chassis/sensor_ray'

    #         ])

    # scan_tf_map = Node(package='tf2_ros', executable='static_transform_publisher',
    #             arguments = [
    #                 '0', '0', '0', '0', '0', '0',
    #                 '/scan',
    #                 'map'
    #         ])


    # lidar_tf_map = Node(package='tf2_ros', executable='static_transform_publisher',
    #             arguments = [
    #                 '0', '0', '0', '0', '0', '0',
    #                 'dolly/chassis/sensor_ray',
    #                 'map'
    #         ])

    # odom_tf_map = Node(package='tf2_ros', executable='static_transform_publisher',
    #             arguments = [
    #                 '0', '0', '0', '0', '0', '0',
    #                 '/dolly/odometry',
    #                 'map'

    #         ])
    # tf_tf= Node(package='tf2_ros', executable='static_transform_publisher',
    #             arguments = [
    #                 '0', '0', '0', '0', '0', '0',
    #                 'odom',
    #                 'base_footprint'

    #         ])    

    # lidar_stf = Node(package='tf2_ros', executable='static_transform_publisher',
    #             arguments = [
    #                 '0', '0', '0', '0', '0', '0', '1',
    #                 'chassis',
    #                 'dolly/chassis/sensor_ray'
    #         ])    

    final_tf1= Node(package='tf2_ros', executable='static_transform_publisher',
                arguments = [
                    '0', '0', '0', '0', '0', '0',
                    'base_footprint',
                    'laser'
            ])

    final_tf2= Node(package='tf2_ros', executable='static_transform_publisher',
                arguments = [
                    '0', '0', '0', '0', '0', '0',
                    'map',
                    'odom'
            ])                   

    final_tf3= Node(package='tf2_ros', executable='static_transform_publisher',
                arguments = [
                    '0', '0', '0', '0', '0', '0',
                    'odom',
                    'base_footprint'

            ])  


    return LaunchDescription([
            DeclareLaunchArgument(
          'ign_args',
          default_value=[os.path.join(pkg_dolly_ignition, 'worlds', 'station.sdf') +
                         ' -v 2 --gui-config ' +
                         os.path.join(pkg_dolly_ignition, 'ign', 'gui.config'), ''],
          description='Ignition Gazebo arguments'),
            DeclareLaunchArgument('use_sim_time', default_value=['true'],
                    description='Enable sim time from /clock'),
            DeclareLaunchArgument('rviz', default_value='true',
                              description='Open RViz.'),
        gazebo,
        spawn,
        # rviz2,
        bridge,
        # state_publisher,
        # tf,
        # lidar_tf,
        # map_tf,
        # odom_tf,
        # scan_tf_map,
        # lidar_tf_map,
        # odom_tf_map,
        # tf_tf
        # lidar_stf 
        final_tf1,
        final_tf2,
        final_tf3 
    ])




  #    <!-- *********************** JOINT STATE PUBLISHER *********************   -->
  
  # <plugin name="dolly_joint_state" filename="libgazebo_ros_joint_state_publisher.so">
  #   <ros>
  #     <remapping>~/out:=joint_states</remapping>
  #   </ros>
  #   <update_rate>30</update_rate>
  #   <joint_name>left_wheel_joint</joint_name>
  #   <joint_name>right_wheel_joint</joint_name>
  # </plugin>  
  #   