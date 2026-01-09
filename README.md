## 🐳 Hello Docker – Flask API Project

This is a simple Python Flask API containerized using Docker. It was built to practice Docker fundamentals like building images, running containers, port mapping, and deploying to Docker Hub.

---

### 📖  Table Of Content
- Features
- Folder Structure
- Projetc Execution
- Cleanup

---
### 🚀 Features

- Two endpoints:
  - `/` returns a hello message
  - `/about` returns project info
- Dockerized with a custom Dockerfile
- Deployable locally or via Docker Hub

---

### 🧱 Folder Structure

```
hello-docker/
├── app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

---
### 💼 Project Execution

**🐍 Step 1: Set Up (Virtual Environment Optional)**

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
pip freeze > requirements.txt
```


**🛠️ Step 2: Build Docker Image**

```
docker build -t hello-docker .
```


**▶️ Step 3: Run the Container**

```
docker run -d -p 5000:5000 --name hello-app hello-docker
```

Visit: http://localhost:5000

🌐 Routes
/ → { "message": "Hello from Docker!" }

/about → project description JSON



**🐳 Step 4: Push to Docker Hub**

- Tag the image using your own dockerhub name
```
docker tag hello-docker njidekadocker/hello-docker:v1
```

- Login to Docker Hub
```
docker login
```

- Push the image
```
docker push njidekadocker/hello-docker:v1 
```



**📂 Step 5: Push to GitHub**

```
git init
git add .
git commit -m "Initial Docker Flask API project"
git remote add origin https://github.com/your-username/hello-docker.git
git push -u origin main
```



### 🧼 Clean Up

```
docker stop hello-app
docker rm hello-app
docker rmi hello-docker
```


#### Built by Jane Obikwelu to learn Docker the fun way 🎉



