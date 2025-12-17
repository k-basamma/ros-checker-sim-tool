# ros-checker-sim-tool
A ROS/ROS2 code checker and simulation preview tool for a 6-DOF robotic arm using Gazebo and a Flask web interface.
# ROS Code Checker & Simulation Preview Tool

## 1. Objective
[cite_start]This project provides a system to validate ROS/ROS2 code nodes for syntax correctness and motion safety before executing them in a robotic simulation environment[cite: 2, 3, 5, 6].

## 2. Project Features
* [cite_start]**Code Checker**: Uses `flake8` for Python syntax validation and custom regex for ROS structure detection[cite: 13, 15].
* [cite_start]**Safety Heuristics**: Detects joint values exceeding safe ranges (+/- 3.14 rad) and checks for proper loop sleep cycles[cite: 16].
* [cite_start]**Simulation Runner**: Launches Gazebo with a 6-DOF robotic arm (UR5) and a pick-and-place scene[cite: 21, 23, 24].
* [cite_start]**Web Interface**: A Flask-based UI for uploading ZIP files, viewing validation reports, and triggering simulations[cite: 33, 34, 35, 36].

## 3. Setup & Installation
### Prerequisites
- Ubuntu 22.04 LTS
- ROS 2 Humble
- Gazebo Classic

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/your-username/ros-checker-sim-tool.git](https://github.com/your-username/ros-checker-sim-tool.git)
   cd ros-checker-sim-tool
