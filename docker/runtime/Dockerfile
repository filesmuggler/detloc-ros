ARG ROS_VERSION

FROM osrf/ros:${ROS_VERSION}-desktop-focal

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

# Source ROS
RUN echo "source /opt/ros/${ROS_VERSION}/setup.bash" >> ~/.bashrc

