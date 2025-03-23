# HackSLUProject
Group memmbers: Ngan (Daisy) Nguyen, Esha Pattan, Gihwan Jung, Luis Palmejar
Sure! Here's a brief README you can use to guide users on how to run your Electron + Flask + Python app:

---

# 📚 SignApp - README

## 🛠 Prerequisites

- **Node.js** and **npm**
- **Python 3.9+** (Anaconda recommended)
- (Optional) **Anaconda** if you use a conda environment.

---

## 🔄 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/DaisyNBN/signapp.git
cd signapp
```

### 2️⃣ Install Node (Electron)
```bash
cd frontend
npm install
```

### 3️⃣ Install Python dependencies
In the project root folder:
```bash
pip install -r requirements.txt
pip install pygame
```

---

## ▶️ How to run the app

### Step 1: Start Flask services

Open two terminals:

**Terminal 1 (for Practice Mode)**  
```bash
cd signapp
python flaskapp.py
```

### Step 2: Start Electron app

In a second terminal:
```bash
cd signapp/frontend
npm start
```

---
