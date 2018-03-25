cmake_minimum_required(VERSION 2.8.3)
project(robert_beverage)

find_package(catkin REQUIRED)

catkin_package()

install(PROGRAMS
  scripts/generate_qr_code
  scripts/web_server
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)