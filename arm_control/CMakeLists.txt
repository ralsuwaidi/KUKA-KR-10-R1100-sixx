cmake_minimum_required(VERSION 2.8.3)
project(arm_control)

find_package(catkin REQUIRED)

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(tests/unit.test)
  add_rostest(tests/integration.test)
endif()