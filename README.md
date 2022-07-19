# void-slam-toolbox
simplified wrapper around slam_toolbox

###These are just raw instructions to replicate the error

IN order to replicate the error follow these steps

`sudo docker build -t stevemacenski/slam_toolbox foxy-devel`


1) `sudo docker run -it <image-id> `
2) `. install/setup.bash`
3) ros2 launch slam-toolbox online_async_launch.py


In another shell in the host, outside the docker 
- check if the slam_toolbox node is visible ie run `ros2 node list`
- if it is not visible, try restarting the system and repeat from step 1

once the node is visible, start building your ros_ws
Clone this repo in the src folder inside your workspace. 
`colcon build --symlink-install ` from the workspace

source install/setup.bash
ros2 launch void-slam-dolly dolly_launch.py

Finally in a new terminal open rviz2

Subscribe to the map topic and lidar scan topic and see the slam-toolbox terminal to view the error
Set map topic to /map
Set lidar scan topic to /scan


