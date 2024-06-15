
# README.md

### Title:
**SMARTDRIVE_YOLOv8**

### Description:
SMARTDRIVE_YOLOv8 is an advanced AI-driven system designed to enhance road safety by dynamically adjusting vehicle speed based on real-time detection of critical road conditions. Utilizing YOLOv8 object detection, this model identifies specific classes such as Bumpy Roads, Construction Work, Hospital Zones, Obstacles(like Blocked roads, Fallen trees, Potholes, Car, Bike,...), Pedestrians, School Zones, and Stop signs. 

Through the use of bounding box coordinates to precisely calculate the distance to each object detected and mathematical computations to estimate speed, the model guarantees timely and appropriate speed adjustments, thereby promoting safer driving environments. The system allows for the input of both images and videos and provides thorough reporting and analysis for better traffic control and speed limit observance.
## Table of Contents

Installation 

Usage

Features

Technologies Used

Contributing

License

Contact
## Installation

#### Prerequisites:
Python 3.7 or higher

pip (Python package installer)

#### Clone the Repository

```bash
  git clone https://github.com/RamyaMN28/AutoSpeedLimit_YOLOv8.git
```
####  Install Required Dependencies

```bash
  pip install -r requirements.txt

```

#### Download YOLOv8 Weights:

Download the YOLOv8 weights from the official repository or link provided in the documentation.


## Deployment


#### Run the Application
```bash
python speed_limitation_image.py

```
```bash
python speed_limitation_video.py

```
## Usage: 

#### Input Source :

The system supports both image and video inputs for comprehensive analysis.

#### Object Detection:

Detects classes including Bumpy Roads, Construction Work, Obstacles(like Blocked roads, Fallen trees, Potholes, Car, Bike,...), Pedestrians(Cyclists, Handicaps, children Strollers,...), School Zones, Hospital Zones and Stop signs. 

#### Distance Calculation:

Utilizes bounding box coordinates to calculate the distance to detected objects.

#### Speed Estimation:

Estimates the vehicle's speed using mathematical calculations.

#### Speed Adjustment:

Dynamically adjusts vehicle speed from the intial speed based on real-time analysis to ensure safer driving conditions.

### Detected Image:

![Screenshot 2024-06-15 213211](https://github.com/RamyaMN28/AutoSpeedLimit_YOLOv8/assets/122740354/c42332ab-6978-4ed2-8b20-0130a57b1085)
![Screenshot 2024-06-15 212806](https://github.com/RamyaMN28/AutoSpeedLimit_YOLOv8/assets/122740354/7a6ffe17-a1df-456b-ae75-55f9ebf746f8)

## Authors

- [@Ramya M N ](https://github.com/RamyaMN28/)

