cmake_minimum_required(VERSION 2.8.3)
project(robert_gazebo)

find_package(catkin REQUIRED)

catkin_package(
  CATKIN_DEPENDS gazebo_ros gazebo_ros_control husky_description
)

install(FILES
  launch/gazebo.launch
  worlds/office.world
  worlds/ucu.world
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
