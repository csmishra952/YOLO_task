
from yolotask.yolo_train import train_yolo
from yolotask.face_features import get_facenet_embeddings
from yolotask.mask_cap_classify import train_classifier, evaluate_classifier

def main():
    # Train YOLOv8
    train_yolo()

    # Example embedding (image_path must exist)
    # embedding = get_facenet_embeddings('example.jpg')

    # ML classification example (dummy)
    # X_train, y_train = ...
    # clf = train_classifier(X_train, y_train)
    # acc = evaluate_classifier(clf, X_test, y_test)
    # print("Classifier accuracy:", acc)

if __name__ == '__main__':
    main()
