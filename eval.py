
def predict_from_yolo(model, image_path):
    results = model(image_path)
    return results
