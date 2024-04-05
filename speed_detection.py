import os
import subprocess
import sys

HOME = os.getcwd()
print(HOME)

import ultralytics
ultralytics.checks()
from ultralytics import YOLO

#CUSTOM TRAINING

yolo_command = "yolo task=detect mode=train model=yolov8s.pt data=data1.yaml epochs=100 imgsz=224 plots=True"

subprocess.run(yolo_command, shell=True)

#VALIDATION

yolo_command = "yolo task=detect mode=val model= runs/detect/train6/weights/best.pt data=data1.yaml"

subprocess.run(yolo_command, shell=True)

#TESTING

yolo_command = "yolo task=detect mode=predict model= runs/detect/train6/weights/best.pt conf=0.25 source=datasets/test save=True"

subprocess.run(yolo_command, shell=True)

#TESTING VIDEO
yolo_command = "yolo task=detect mode=predict model=runs/detect/train6/weights/best.pt conf=0.25 source=testing/vid4.mp4 save=True"

subprocess.run(yolo_command, shell=True)

#TESTING IMAGE
yolo_command = "yolo task=detect mode=predict model=runs/detect/train6/weights/best.pt conf=0.25 source=testing/img9.png save=True"  

subprocess.run(yolo_command, shell=True)



####################################################################
'''
import subprocess
import torch
from PIL import Image
from pathlib import Path
from utils.general import non_max_suppression, scale_coords
from models.experimental import attempt_load
from utils.datasets import letterbox

def adjust_speed(current_speed, detected_sign):
    speed_adjustments = {
        "Pedestrian": 10, 
        "Children crossing": 20, 
        "Stop": 30,  
        "No passing": 40,  
        "No passing veh over 3.5 tons": 40, 
    }
    
    speed_adjustment = speed_adjustments.get(detected_sign, 0)
    
    new_speed = current_speed - speed_adjustment
    if new_speed < 0:
        new_speed = 0 
    
    return new_speed

# Define the YOLO command as a string
yolo_command = "yolo task=detect mode=predict model=runs/detect/train2/weights/best.pt conf=0.25 source=testing/img4.png save=True"

# Execute the YOLO command using subprocess
subprocess.run(yolo_command, shell=True)

# Load the detected image from the save directory
detected_img_path = "runs/detect/train2/img4.png"  # Change this path accordingly
detected_img = Image.open(detected_img_path)

# Load YOLOv8 model
model = attempt_load("yolov8.pt", map_location=torch.device('cpu'))

# Inference
detected_img = letterbox(detected_img, 640, stride=32)[0]
detected_img = torch.from_numpy(detected_img).to('cpu')
detected_img = detected_img.float() / 255.0
if detected_img.ndimension() == 3:
    detected_img = detected_img.unsqueeze(0)

pred = model(detected_img)[0]
pred = non_max_suppression(pred, 0.4, 0.5)

# Extract detected traffic signs
detected_signs = []
for det in pred[0]:
    if det is not None:
        det[:, :4] = scale_coords(detected_img.shape[2:], det[:, :4], detected_img.shape).round()
        for *xyxy, conf, cls in det:
            label = model.names[int(cls)]
            if 'traffic sign' in label:
                detected_signs.append(label)

# Process detected signs
if detected_signs:
    current_speed = float(input("Enter your current speed (in km/h): "))
    detected_sign = detected_signs[0]  # Assuming we only process the first detected sign
    confidence = 1.0  # You may calculate confidence based on model's output

    speed_limit = None
    if "Speed limit" in detected_sign:
        speed_limit = detected_sign.split("(")[1].split(")")[0]

    adjusted_speed = adjust_speed(current_speed, detected_sign)

    print("Predicted traffic sign:", detected_sign)
    print("Predicted speed limit:", speed_limit)
    print("Confidence:", confidence)
    print("Adjusted speed:", adjusted_speed, "km/h")
else:
    print("No traffic sign detected in the image.")
'''