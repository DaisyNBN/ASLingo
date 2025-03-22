import tkinter as tk
from PIL import Image, ImageTk
import torch
from torchvision import models, transforms
import cv2
import numpy as np

# === ASL Classes ===
class_names = sorted([
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'del', 'nothing', 'space'
])

# === Load Model ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18()
model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
state_dict = torch.load('asl_resnet18.pth', map_location=device, weights_only=True)
model.load_state_dict(state_dict)
model.to(device)
model.eval()

# === Preprocessing ===
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# === Predict Function ===
def predict_frame(frame):
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).convert('RGB')
    input_tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(input_tensor)
        _, pred = torch.max(output, 1)
        return class_names[pred.item()]

# === GUI Setup ===
root = tk.Tk()
root.title("ASL Webcam Classifier")
root.geometry("500x600")

label = tk.Label(root, text="Live ASL Prediction", font=("Arial", 16))
label.pack(pady=10)

img_label = tk.Label(root)
img_label.pack()

prediction_label = tk.Label(root, text="", font=("Arial", 20), fg="blue")
prediction_label.pack(pady=10)

# === Webcam Setup ===
cap = cv2.VideoCapture(0)

def update_frame():
    ret, frame = cap.read()
    if ret:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        imgtk = ImageTk.PhotoImage(image=img.resize((400, 300)))
        img_label.imgtk = imgtk
        img_label.configure(image=imgtk)
    root.after(10, update_frame)

# === Capture and Predict ===
def capture_and_predict():
    ret, frame = cap.read()
    if ret:
        pred = predict_frame(frame)
        prediction_label.config(text=f"Prediction: {pred}")

btn = tk.Button(root, text="Capture Image", command=capture_and_predict, font=("Arial", 14))
btn.pack(pady=20)

update_frame()
root.mainloop()

cap.release()
