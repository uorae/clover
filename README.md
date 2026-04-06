# 🍀 clover cam (wip)
a program that finds four leaf clovers in a field of three-leaf clovers<br>
built using YOLOv11 and OpenCV

<!-- ## Demo -->

### Installation
git clone<br>
cd clover-cam<br>
python -m venv clover-env<br>
source clover-env/Scripts/activate<br>
pip install -r requirements.txt<br>

### Dataset
compiled from my own images and existing datasets on roboflow (linked in `data.yaml`)<br>
export train, valid and test folders in YOLOv11 format and place in the project root before training.<br>

### Training
python main.py

<!-- ## Usage
python app.py -->

### Results
0.76 mAP50 achieved after first train