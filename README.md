# YOLO Task: Face Detection & Classification

This project demonstrates a modular ML pipeline combining **YOLOv8** for face detection and **FaceNet** embeddings for face analysis (mask/cap classification).

## Structure

- `yolotask/`: Core module
- `main.py`: Entry point
- `data/`: Place your dataset here

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Requirements

- YOLOv8 (via `ultralytics`)
- FaceNet (via `facenet-pytorch`)
- scikit-learn, torch, torchvision
