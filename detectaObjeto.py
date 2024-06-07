import cv2
from ultralytics import YOLO

model = YOLO("C:/Users/jeffe/pi2/runs/detect/train/weights/best.pt")

# Abrir uma conexão com a câmera
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Camera nao encontrada")
    exit()

# Ler um frame da câmera
sucess, frame = cap.read()

if not sucess:
    print("Can't receive frame (stream end?). Exiting ...")
    exit()

classNames = {0: "AZUL", 1: "AMARELO", 2: "PRETO"}

# Realizar a detecção
result = model(frame, save=True)

# Extrair classes e acurácias das detecções
if len(result) > 0:
    boxes = result[0].boxes
    confidences = boxes.conf.tolist() if boxes.conf is not None else []
    classes = boxes.cls.tolist() if boxes.cls is not None else []

    for cls in classes:
        cls_int = int(cls)  # Converter para inteiro
        if cls_int in classNames:
            confidence = confidences[classes.index(cls)]
            print(f"Classe identificada: {classNames[cls_int]} (Confiança: {confidence:.2f})")

else:
    print("No detections found.")

# Liberar a câmera
cap.release()
