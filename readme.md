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

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/pdf-audiobook.git
cd pdf-audiobook
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🐳 Docker

### Build the image
```bash
docker build -t aliyafirdous22/pdf-audiobook:v1 .
```

### Run the container
```bash
docker run -p 8501:8501 aliyafirdous22/pdf-audiobook:v1
```

### Push to Docker Hub
```bash
docker login
docker push aliyafirdous22/pdf-audiobook:v1
```

🔗 Docker Hub: `https://hub.docker.com/r/aliyafirdous22/pdf-audiobook`

---

## ☸️ Kubernetes with Minikube

### Start Minikube
```bash
minikube start --memory=2048mb --cpus=2
```

### Deploy the app
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Check pods are running
```bash
kubectl get pods
kubectl get services
```

### Access the app
```bash
kubectl port-forward service/pdf-audiobook-service 8501:80
```

Then open `http://localhost:8501`

---

## 📈 Scaling with Kubernetes

One of the biggest advantages of Kubernetes is scaling.
You can run multiple copies of the app at the same time:
```bash
# Scale up to 5 replicas
kubectl scale deployment pdf-audiobook --replicas=5

# Check all pods running
kubectl get pods

# Scale back down
kubectl scale deployment pdf-audiobook --replicas=2
```

This means if 100 people use the app at the same time,
Kubernetes distributes the load across all replicas automatically.

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

## 🎯 Use Case

> You have a 50-page research paper to read before tomorrow's class.
> Instead of reading it, just upload it to PDF Audio-Book,
> download the MP3, and listen while getting ready, eating,
> or traveling. Learn without stopping your day! 🎧

---

## 👩‍💻 Author

**Aliya Firdous**  
Built with Python • Containerized with Docker • Scaled with Kubernetes