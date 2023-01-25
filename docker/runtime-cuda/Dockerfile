FROM nvcr.io/nvidia/pytorch:22.12-py3

# LABELs
LABEL maintainer="krzysztof.stezala@put.poznan.pl"

# ARGuments
ARG DEBIAN_FRONTEND=noninteractive
ARG NAME
ARG BUILD_VERSION
ARG BUILD_DATE
ARG DESCRIPTION
ARG URL
ARG DOCKER_CMD
ARG ROS_VERSION


# Set up labels
LABEL org.label-schema.name=${NAME}
LABEL org.label-schema.schema-version=${BUILD_VERSION}
LABEL org.label-schema.build-date=${BUILD_DATE}
LABEL org.label-schema.description=${DESCRIPTION}
LABEL org.label-schema.url=${URL}
LABEL org.label-schema.docker.cmd=${DOCKER_CMD}

# Minimal setup
RUN apt-get update \
    && apt-get install -y \
    locales lsb-release openssh-server nano gnupg \
    software-properties-common curl git apt-transport-https

# Update locales
RUN locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    LANG=en_US.UTF-8 && \
    dpkg-reconfigure locales \
    locales

# Add new repository for ROS
RUN add-apt-repository universe && \
    apt update && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb http://packages.ros.org/ros2/ubuntu focal main" > /etc/apt/sources.list.d/ros2.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# Install ROS foxy
RUN apt update && \
    apt upgrade -y && \
    apt install -y ros-${ROS_VERSION}-desktop python3-argcomplete ros-dev-tools

# Source ROS
RUN echo "source /opt/ros/${ROS_VERSION}/setup.bash" >> ~/.bashrc




