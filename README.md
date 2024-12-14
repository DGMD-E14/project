# **Autonomous Mars Rover Navigation System**

## **Project Overview**  
This project develops an **autonomous navigation system** for a Mars rover capable of detecting obstacles, planning optimized paths, and visualizing results on Martian terrain images. Using **computer vision**, **machine learning**, and the **A\*** pathfinding algorithm, the system simulates efficient navigation around obstacles to reach a defined goal.

The project uses publicly available terrain data from NASA's **AI4MARS** dataset to train and validate the system.

---

## **Features**  
- **Obstacle Detection**: Identifies large obstacles using **Canny Edge Detection** and **Contour Analysis**.  
- **Pathfinding**: Implements the **A\*** algorithm to compute collision-free and efficient paths on a grid-based map.  
- **Visualization**: Overlays the path, start, and goal points on original terrain images for easy interpretation.  
- **Modular Design**: Code is split into reusable components for detection, pathfinding, and visualization.

---

## **Data Source**  
The original dataset used for this project is the **AI4MARS Dataset**, provided by NASA.  
Access it here: [**AI4MARS: A Dataset for Terrain-Aware Autonomous Driving**](https://data.nasa.gov/Space-Science/AI4MARS-A-Dataset-for-Terrain-Aware-Autonomous-Dri/cykx-2qix/data).  

This dataset contains annotated terrain images captured by the **Curiosity Rover** on Mars, making it suitable for obstacle detection and navigation tasks.

---

## **Requirements**  
Ensure the following tools and libraries are installed:  

- Python 3.8+  
- TensorFlow / Keras  
- OpenCV  
- NumPy  
- Matplotlib  
