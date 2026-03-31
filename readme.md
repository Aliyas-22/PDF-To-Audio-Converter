# 🎧 PDF Audio-Book Converter

A Python-based web application that converts PDF documents into audio,
so you can **listen to your documents** instead of reading them.
Perfect for when you're busy, commuting, cooking, or just want to
give your eyes a rest!

---

## 💡 The Idea

Ever had a long PDF to read but no time to sit and read it?
This app solves that — just upload your PDF and it converts it
into an MP3 audio file you can listen to anywhere, anytime.

> You have a 50-page research paper to read before tomorrow's class.
> Instead of reading it, just upload it to PDF Audio-Book,
> download the MP3, and listen while getting ready, eating,
> or traveling. Learn without stopping your day! 🎧

---

## ✨ Features

- 📄 Upload any PDF document
- 🔍 Automatically extracts and cleans text
- 🔊 Play audio directly in the app
- 💾 Download as MP3 file
- 🎚️ Adjust speaking speed and volume
- 100% works in your browser — no extra software needed

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI |
| PyPDF | PDF text extraction |
| pyttsx3 | Text to speech conversion |
| Docker | Containerization |
| Kubernetes (Minikube) | Orchestration & scaling |

---

## 📁 Project Structure
```
pdf-audiobook/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image instructions
├── deployment.yaml     # Kubernetes deployment config
└── service.yaml        # Kubernetes service config
```

---

## ▶️ Option 1 — Run Locally (Simplest Way)

Follow these steps one by one:

**Step 1: Clone the project**
```bash
git clone https://github.com/Aliyas-22/PDF-To-Audio-Converter.git
cd PDF-To-Audio-Converter
```

**Step 2: Create a virtual environment**
```bash
python -m venv venv
```

**Step 3: Activate the virtual environment**
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**Step 4: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 5: Run the app**
```bash
streamlit run app.py
```

**Step 6: Open in browser**
```
http://localhost:8501
```

**Step 7: Use the app**
- Upload your PDF using the file uploader
- Wait for text to be extracted
- Click **Generate MP3** to download your audio file
- Adjust speed and volume from the left sidebar

---

## 🐳 Option 2 — Run with Docker

**Step 1: Make sure Docker is installed**
```bash
docker --version
```

**Step 2: Pull the image from Docker Hub**
```bash
docker pull aliyafirdous22/pdf-audiobook:v1
```

**Step 3: Run the container**
```bash
docker run -p 8501:8501 aliyafirdous22/pdf-audiobook:v1
```

**Step 4: Open in browser**
```
http://localhost:8501
```

---

## ☸️ Option 3 — Run with Kubernetes (Minikube)

**Step 1: Make sure you have these installed**
- Docker
- Minikube
- kubectl

**Step 2: Start Minikube**
```bash
minikube start --memory=2048mb --cpus=2
```

**Step 3: Deploy the app**
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

**Step 4: Check pods are running**
```bash
kubectl get pods
```
Wait until status shows `Running`

**Step 5: Access the app**
```bash
kubectl port-forward service/pdf-audiobook-service 8501:80
```

**Step 6: Open in browser**
```
http://localhost:8501
```

---

## 📈 Scaling with Kubernetes

Kubernetes lets you run multiple copies of the app at the same time.
If many people use the app together, Kubernetes handles the load automatically.
```bash
# Scale up to 5 replicas
kubectl scale deployment pdf-audiobook --replicas=5

# Check all pods running
kubectl get pods

# Scale back down
kubectl scale deployment pdf-audiobook --replicas=2
```

---

## 👩‍💻 Author

**Aliya Firdous**  
Built with Python • Containerized with Docker • Scaled with Kubernetes
