# Use Ubuntu 24.04 as the base image
   FROM ubuntu:24.04
   
   # Set non-interactive mode for the installation
   ENV DEBIAN_FRONTEND=noninteractive
   
   # Install base dependencies
   RUN apt-get update && apt-get install -y \
   curl \
   gnupg2 \
   lsb-release \
   software-properties-common \
   build-essential \
   cmake \
   git
   
   # Add the ROS 2 package repository and its key
   RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
   sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list' && \
   apt-get update && apt-get install -y ros-jazzy-desktop
   
   # Install Gazebo vendor packages
   RUN export ROS_DISTRO=jazzy && \
   apt-get install -y \
   ros-${ROS_DISTRO}-gz-tools-vendor \
   ros-${ROS_DISTRO}-gz-sim-vendor
   
   # Add ROS 2 repository and install ROS and Gazebo vendor packages
   RUN apt-get update && apt-get install -y \
   ros-jazzy-gz-tools-vendor \
   ros-jazzy-gz-sim-vendor

   # Source the ROS 2 setup
   RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
   
   # Add the command to source the environment and allow running `gz sim`
   CMD ["bash", "-c", "source /opt/ros/jazzy/setup.bash && bash"]
