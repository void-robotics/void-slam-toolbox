from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

	obstacle_avoidance = Node(
		package='void-slam-dolly',
		executable= 'obstacle_avoidance',
		output='screen',
		remappings=[
		('laser_scan','/scan'),
		('cmd_vel','/dolly/cmd_vel')
		]
	)

	#This remappiing is of original ros topics and your model topic

	# Since inside the node definitions we take use of ros sensor msgs head file, which by default have laser_scan and all those topics
	# we need to manually tell the node thrugh launch files that,  instead of publishing or subscribing the data from the ros topics
	# subscribe through our model's sensor topic which we defined in the sdf files

	#Also you need remapping in the node launching and not at the bridge launch

	#executables have to be defined in the Cmake llist
	# in order to define an executable you need to create a node of some functionality which will later be used and instatiate in Cmake 

	return LaunchDescription([
		obstacle_avoidance
	]);


#since launch folder will be installed so you don't have to add an executable for the launch files just if you want to run the node directly


