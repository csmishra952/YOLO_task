
from ultralytics import YOLO

def train_yolo(model_path='yolov8n.pt', data_yaml='data.yaml', epochs=20, imgsz=640):
    model = YOLO(model_path)
    results = model.train(data=data_yaml, epochs=epochs, imgsz=imgsz)
    return results
