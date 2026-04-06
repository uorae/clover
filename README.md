# 🍀 clover cam (wip)
a program that finds four leaf clovers in a field of three-leaf clovers
built using YOLOv11 and OpenCV

<!-- ## Demo -->

## Installation
git clone
cd clover-cam
python -m venv clover-env
source clover-env/Scripts/activate
pip install -r requirements.txt

## Dataset
compiled from my own images and existing datasets on roboflow (linked in `data.yaml`)
export train, valid and test folders in YOLOv11 format and place in the project root before training.

## Training
python main.py

<!-- ## Usage
python app.py -->

## Results
0.76 mAP50 achieved after first train