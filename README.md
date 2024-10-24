# ROS 2 Jazzy Jalisco and Gazebo Harmonic Setup on macOS using Docker

This guide helps you set up **Ubuntu 24.04 (Noble)**, **ROS 2 Jazzy Jalisco**, and **Gazebo Harmonic** on macOS using Docker.

## Prerequisites

- **Docker Desktop** installed on macOS
    - [Download Docker](https://www.docker.com/products/docker-desktop)
- (Optional) **XQuartz** for GUI applications like Gazebo
    - [Download XQuartz](https://www.xquartz.org/)

## Step 1: Install Docker Desktop

1. Download **Docker Desktop** for macOS from the [official website](https://www.docker.com/products/docker-desktop).
2. Install Docker by following the instructions provided.
3. Verify that Docker is installed correctly by running:
   ```bash
   docker --version

You should see the installed Docker version in the terminal.

## Step 2: Set Up Ubuntu Noble 24.04 in Docker

1. Create a working directory for the Docker project:
   ```bash
    mkdir ros2_gazebo_setup && cd ros2_gazebo_setup
2. Create and edit the Dockerfile using nano:
    ```bash
    nano Dockerfile
   ```
   This will open the nano editor. You can then paste the content of the Dockerfile into the editor.
3. Paste the following content into nano:
   ```dockerfile
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
4. Save and exit nano:
-  After pasting the content, press Ctrl + O to write (save) the file.
- Press Enter to confirm the file name (Dockerfile).
- Press Ctrl + X to exit nano.
5. Verify that the Dockerfile is created:
   ```bash
   ls
   ```
    You should see the Dockerfile in the working directory.
6. Build the Docker image using the Dockerfile:
   ```bash
   docker build -t ros2_gazebo_harmonic .

## Step 3: Run the Docker Container

1. Once the image is built, you can run the container and source the ROS environment to use Gazebo commands:
   ```bash
   docker run -it ros2_gazebo_harmonic bash
This will start an interactive bash session inside the container. Since the environment is sourced through .bashrc, you should have access to the gz commands (Gazebo command-line tools).
To ensure that Gazebo is correctly installed and available via the gz command, you can run:
   ```bash
   gz sim --help
   ```
This will display the help for the Gazebo simulation tool, verifying that the Gazebo vendor packages are installed and working properly.

2. You are now inside the Docker container with **Ubuntu 24.04**, **ROS 2 Jazzy Jalisco**, and **Gazebo Harmonic** installed.

3. Source the ROS 2 environment:
   ```bash
   source /opt/ros/jazzy/setup.bash

## Step 4: Running ROS 2 and Gazebo

**Running ROS 2:**

1. Test ROS 2 by running:
   ```bash
   ros2 topic list

**Running Gazebo:**

1. Start Gazebo by running:
   ```bash
   gz sim

2. To display the GUI for Gazebo on macOS, ensure **XQuartz** is installed and running.
3. Set up the display environment variable:
   ```bash
   export DISPLAY=:0

4. Start the Docker container with GUI support:
   ```bash
   docker run -it --rm -e DISPLAY=host.docker.internal:0 ros2_gazebo_harmonic bash

## Step 5: Save Your Docker Work
Once you’re done, you can save your Docker container state as a new image:
```bash
    docker commit ros2_gazebo_harmonic ros2_gazebo_setup_image
```
You can now reuse this image for future projects without having to reinstall ROS 2 and Gazebo.

## Additional Notes
- **ROS 2 Jazzy Jalisco** and **Gazebo Harmonic** are under active development. Ensure you update your Docker image periodically to get the latest updates and patches.
- For more information on using Docker with ROS, visit [ROS Docker Hub](https://hub.docker.com/_/ros).
- For more information about Gazebo, visit the [Gazebo Documentation](https://gazebosim.org/docs/latest/ros_installation/).