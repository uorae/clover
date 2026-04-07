import sys
import cv2
from ultralytics import YOLO

if len(sys.argv) < 2:
  print("Usage: python main.py <video_path>")
  sys.exit(1)

# Load the YOLO model
model = YOLO("best.pt")

# Open the video file
video_path = sys.argv[1]  # Get the video path from command line arguments

try:
  cap = cv2.VideoCapture(video_path)
except:
  print("Error: Could not open video file.")
  sys.exit(1)

# Loop through the video frames
while cap.isOpened():
  # Read a frame from the video
  success, frame = cap.read()

  if success:
    # Run YOLO inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLO Inference", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
  else:
    # Break the loop if the end of the video is reached
    break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()