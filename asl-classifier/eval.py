import os
import torch
from torchvision import models, transforms
from PIL import Image

# Paths
test_dir = 'data/asl_alphabet_test/asl_alphabet_test'
model_path = 'asl_resnet18.pth'
class_names = sorted([
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'del', 'nothing', 'space'
])  # must match training order!

# Transforms (same as training)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# Load model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18()
model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
state_dict = torch.load('asl_resnet18.pth', map_location=device, weights_only=True)
model.load_state_dict(state_dict)
model.to(device)
model.eval()

# Predict each test image
for filename in sorted(os.listdir(test_dir)):
    if filename.endswith('.jpg'):
        img_path = os.path.join(test_dir, filename)
        image = Image.open(img_path).convert('RGB')
        input_tensor = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            output = model(input_tensor)
            _, pred = torch.max(output, 1)
            predicted_class = class_names[pred.item()]
        
        print(f"{filename:<20} → Prediction: {predicted_class}")
