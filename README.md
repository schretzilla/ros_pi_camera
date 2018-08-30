This package contains simple code for publishing image data from a raspberry pi camera to a topic as well as listening to that topic and displaying that data.

If creating a ROS package from scratch

catkin_create_pkg pi_camera std_msg rospy roscpp sensor_msgs cv_bridge roscpp std_msgs image_transport


Copy the provided scripts into the pi_camera/scripts directory
run catkin_make 

