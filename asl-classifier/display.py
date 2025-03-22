import torch
from torchvision import models, transforms
from PIL import Image
import matplotlib.pyplot as plt
import sys
import os

# === Config ===
test_folder = 'data/test'  # Replace this
model_path = 'asl_resnet18.pth'

# === ASL Classes ===
class_names = sorted([
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'del', 'nothing', 'space'
])

# === Preprocessing ===
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# === Load Model ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18()
model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
state_dict = torch.load('asl_resnet18.pth', map_location=device, weights_only=True)
model.load_state_dict(state_dict)
model.to(device)
model.eval()


for filename in sorted(os.listdir(test_folder)):
    if filename.endswith('.jpg'):
        img_path = os.path.join(test_folder, filename)

        # Load & preprocess image
        image = Image.open(img_path).convert('RGB')
        input_tensor = transform(image).unsqueeze(0).to(device)

        # Predict
        with torch.no_grad():
            output = model(input_tensor)
            _, pred = torch.max(output, 1)
            predicted_class = class_names[pred.item()]

        # Display
        print(f"{filename:<20} → Prediction: {predicted_class}")
        plt.imshow(image)
        plt.title(f"{filename} → {predicted_class}", fontsize=14)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
