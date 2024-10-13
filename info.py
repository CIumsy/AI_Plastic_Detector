from ultralytics import YOLO

# Load the model
model = YOLO('best.pt')

# Display model details
model.info()
