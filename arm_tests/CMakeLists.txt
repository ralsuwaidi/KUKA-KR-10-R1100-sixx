cmake_minimum_required(VERSION 2.8.3)
project(arm_tests)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
