# detloc-ros
Versatile detection and localization pipeline in ROS for deep learning models

# Docker
## Build images

```sh
docker compose build --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
```

## Build and run containers

```sh
docker compose up --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
```

## User

```sh
xhost +local:root
docker run -it --net=host --name=dlr-user-container docker-dlr-user /bin/bash
```

## Runtime

```sh
docker run -it --net=host --name=dlr-runtime-container docker-dlr-runtime /bin/bash
```
