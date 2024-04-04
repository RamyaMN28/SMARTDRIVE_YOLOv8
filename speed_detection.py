import os
import subprocess
import sys

HOME = os.getcwd()
print(HOME)

import ultralytics
ultralytics.checks()
from ultralytics import YOLO

import subprocess

# Define the YOLO command as a string
yolo_command = "yolo task=detect mode=train model=yolov8s.pt data=data1.yaml epochs=5 imgsz=224 plots=True"

# Execute the YOLO command using subprocess
subprocess.run(yolo_command, shell=True)


# Define the YOLO command as a string
yolo_command = "yolo task=detect mode=val model= runs/detect/train3/weights/best.pt data=data1.yaml"

# Execute the YOLO command using subprocess
subprocess.run(yolo_command, shell=True)

# Define the YOLO command as a string
yolo_command = "yolo task=detect mode=predict model= runs/detect/train3/weights/best.pt conf=0.25 source= datasets/test save=True"

# Execute the YOLO command using subprocess
subprocess.run(yolo_command, shell=True)


# Define the YOLO command as a string
yolo_command = "yolo task=detect mode=predict model=runs/detect/train3/weights/best.pt conf=0.25 source=testing/videoo.mp4 save=True"

# Define the YOLO command as a string
yolo_command = "yolo task=detect mode=predict model=runs/detect/train2/weights/best.pt conf=0.25 source=testing/img4.png save=True"

# Execute the YOLO command using subprocess
subprocess.run(yolo_command, shell=True)