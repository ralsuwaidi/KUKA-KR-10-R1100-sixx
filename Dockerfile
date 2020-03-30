# from https://github.com/henry2423/docker-ros-vnc/blob/master/Dockerfile
FROM henry2423/ros-vnc-ubuntu:melodic

ENV DEBIAN_FRONTEND noninteractive

# dependancies
RUN apt-get update && apt-get install ros-melodic-gazebo-ros-pkgs -y

# catkin ws
ENV CATKIN_WS=/root/catkin_ws

RUN sh -c 'mkdir -p ${CATKIN_WS}/src && \
    cd ${CATKIN_WS}/src && \
    git clone https://github.com/dankirsdot/KUKA-KR-10-R1100-2.git'

# make
RUN sh -c 'source /opt/ros/melodic/setup.bash && cd ${CATKIN_WS} && \
    catkin_make'

# vnc ports
ENV DISPLAY=:1 \
    VNC_PORT=5901 \
    NO_VNC_PORT=6901
EXPOSE $VNC_PORT $NO_VNC_PORT

## Envrionment config
ENV VNCPASSWD=vncpassword
ENV HOME=/home/$USER \
    TERM=xterm \
    STARTUPDIR=/dockerstartup \
    INST_SCRIPTS=/home/$USER/install \
    NO_VNC_HOME=/home/$USER/noVNC \
    DEBIAN_FRONTEND=noninteractive \
    VNC_COL_DEPTH=24 \
    VNC_RESOLUTION=1920x1080 \
    VNC_PW=$VNCPASSWD \
    VNC_VIEW_ONLY=false
WORKDIR $HOME