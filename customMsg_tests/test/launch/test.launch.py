from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='test',
            executable='Node1.py',
            name='node1'
        ),

    # customize launch file below
    #heheheheheheheheh
    # end launch file customization
    ])
