from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    detection_node = Node(
        package="detection_node",
        executable="detection_node"
    )

    ld.add_action(detection_node)

    return ld


