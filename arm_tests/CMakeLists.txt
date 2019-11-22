cmake_minimum_required(VERSION 2.8.3)
project(arm_tests)

find_package(catkin REQUIRED)

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(launch/gazebo.test)
endif()

catkin_package()

install(DIRECTORY scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
