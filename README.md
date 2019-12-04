# KUKA-KR-10-R1100 sixx

[![Build Status](https://travis-ci.com/dankirsdot/KUKA-KR-10-R1100-sixx.svg?branch=badges)](https://travis-ci.com/dankirsdot/KUKA-KR-10-R1100-sixx)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dankirsdot/KUKA-KR-10-R1100-sixx/issues)
[![HitCount](http://hits.dwyl.io/dankirsdot/KUKA-KR-10-R1100-sixx.svg)](http://hits.dwyl.io/dankirsdot/KUKA-KR-10-R1100-sixx)

Initially I wanted to make model of EvoArm - open-source, 3D-printable, desktop-sized, 3+2DOF robot arm. This is a manipulator with a closed kinematic chain and to describe it it was necessary to make an sdf model. In the process, I ran into significant difficulties, and also found that the sdf model cannot be used with other parts of ROS except Gazebo. Because of this, I took another robot for modeling - KUKA-KR-10-R1100 sixx. I took STL models of its parts, as well as several useful solutions (colors.xacro, materials.xacro, constants.xacro) from the repository [kuka_experimental](https://github.com/ros-industrial/kuka_experimental). The main part of my model, I wrote myself. All the necessary data (the limits of the joints and default colors) I took from [robot datasheet](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=2ahUKEwjyte-SyvbkAhVitIsKHffOCe0QFjABegQIABAC&url=https%3A%2F%2Fwww.kuka.com%2F-%2Fmedia%2Fkuka-downloads%2Fimported%2F48ec812b1b2947898ac2598aff70abc0%2Fspez_kr_agilus_sixx_en.pdf%3Frev%3D9d85bafa3245437884ad99be3a14732b%3Fmodified%3D1052831294&usg=AOvVaw0il71PLMTRAFlnoxJVXnOM), the weights of the parts, as well as the inertia tensors I took [here](https://dspace.cvut.cz/bitstream/handle/10467/69940/F3-BP-2017-Woller-David-automatic%20planning%20of%20robot%20motion.pdf).

To use the package, open a terminal and do the following:

## Install ROS Melodic

```bash
# enable all Ubuntu packages:
$ sudo apt-add-repository universe
$ sudo apt-add-repository multiverse
$ sudo apt-add-repository restricted

# add ROS repository to apt sources
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116

# install ROS Base
$ sudo apt-get update
$ sudo apt-get install ros-melodic-ros-base

# add ROS paths to environment
sudo sh -c 'echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc'
```

Close and restart the terminal.

## Build the model

```bash
$ cd ~/catkin_workspace/
$ git clone https://github.com/dankirsdot/KUKA-KR-10-R1100-2.git
$ catkin_make
$ source devel/setup.bash
```

## Show the model

You can use Rviz
```bash
$ roslaunch arm_show rviz.launch
```
or Gazebo launch files
```bash
$ roslaunch arm_show gazebo.launch
```

## Run robot control

You can run the simulation with the python control script using the following command:
```bash
$ roslaunch arm_control control.launch
```

You can also add the camera to the arm with the following command:
```bash
$ roslaunch arm_control control.launch is_using_camera:=true
```

Example of robot movements is [here](https://youtu.be/r0B7GUYYAzM)

## Run tests

To run unit and integration tests use the following command
```bash
$ catkin_make run_tests && catkin_test_results
```


### Enjoy!
