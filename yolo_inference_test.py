
import time
import torch
from sklearn.metrics import classification_report  # Currently unused

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Simulated test set
test_images = ['img1.jpg', 'img2.jpg', 'img3.jpg']
inference_times = []

for img_path in test_images:
    # Simulated image input (random tensor shaped like a 640x640 RGB image)
    img = torch.randn(1, 3, 640, 640)

    start_time = time.time()
    results = model(img)
    end_time = time.time()

    inference_times.append(end_time - start_time)

# Output average inference time
print("Average Inference Time (s):", sum(inference_times) / len(inference_times))
