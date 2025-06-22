# 🚀 CI/CD Flask App with Docker

This project demonstrates how to build a simple Flask web application, Dockerize it, and prepare it for CI/CD workflows. It's a great starting point for deploying Python web apps in containerized environments.

---

## 📁 Project Structure

```
ci-cd-flask-app/
├── app.py              # Main Flask app
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image build instructions
├── test_app.py         # Unit test for the app
```

---

## 🔧 Prerequisites

Ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)
- `pytest` for testing:
  ```bash
  pip install pytest
  ```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ci-cd-flask-app.git
cd ci-cd-flask-app
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Run Unit Tests

```bash
pytest test_app.py
```

This will run a simple test to verify that the Flask app returns the correct response.

---

## 🐍 Run Flask App Locally

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🐳 Docker Usage

### Build Docker Image

```bash
docker build -t yourdockerhubusername/flask-cicd-app:latest .
```

### Run Docker Container

```bash
docker run -p 5000:5000 yourdockerhubusername/flask-cicd-app:latest
```

Then access the app at [http://localhost:5000](http://localhost:5000)

---

## ✅ Future Enhancements

- Add CI/CD automation using GitHub Actions or GitLab CI
- Add production-ready configurations (e.g., Gunicorn, Nginx)
- Add environment variable management using `.env`
- Implement test coverage reports and advanced test cases

---

## 📄 License

This project is licensed under the MIT License.
