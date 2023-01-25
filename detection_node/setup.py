from setuptools import setup

package_name = 'detection_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='filesmuggler',
    maintainer_email='krzysztof.stezala@put.poznan.pl',
    description='Performs detection over images from the camera topic.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detection_node = detection_node.DetectionNode:main',
        ],
    }
)
