import numpy as np
import cv2 as cv
from ultralytics import YOLO
 
model = YOLO("best.pt")
try:
  cap = cv.VideoCapture(0)
except:
  print("Cannot open camera")
  exit()

while True:
  # Capture frame-by-frame
  ret, frame = cap.read()

  # if frame is read correctly ret is True
  if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break
  # Our operations on the frame come here
  results = model(source=frame, show=True, stream=True)
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()