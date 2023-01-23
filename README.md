# detloc-ros
Versatile detection and localization pipeline in ROS for deep learning models


# Development

## Setup workspace
On the PC create directory structure:
```sh
mkdir -p ~/detloc_ws/src
```
Clone necessary repos into the source folder:
```sh
cd ~/detloc_ws/src
git clone -b foxy_devel https://github.com/filesmuggler/detloc-ros
git clone -b foxy https://github.com/ros-perception/vision_msgs
```

## Docker environment
Run docker containers as specified in `docker` branch