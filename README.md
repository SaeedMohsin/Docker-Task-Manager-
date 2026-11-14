# 🐳 Docker Task Manager

A containerized Task Manager REST API built using **Python Flask, PostgreSQL, Docker, Docker Compose, and Nginx**.

This project demonstrates practical DevOps concepts, including containerization, multi-container orchestration, networking, persistent storage, health checks, automated backups, and Continuous Integration.

## 🏗️ Architecture

```text
             Client / Browser
                    |
                    v
               Nginx :8080
                    |
                    v
              Flask API :5000
                    |
                    v
             PostgreSQL :5432
                    |
                    v
              Docker Volume
```

## 🚀 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | REST API framework |
| PostgreSQL | Relational database |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| Nginx | Reverse proxy |
| Docker Volumes | Persistent database storage |
| Docker Networks | Container communication |
| Health Checks | Container health monitoring |
| Bash | Database backup automation |
| Pytest | Automated testing |
| Git & GitHub | Version control |
| GitHub Actions | Continuous Integration |

## ✨ Features

- Create new tasks
- Retrieve all tasks
- Update existing tasks
- Delete tasks
- PostgreSQL database integration
- Persistent database storage
- Nginx reverse proxy
- Docker health checks
- Separate frontend and backend networks
- Automated database backup script
- Automated application tests
- GitHub Actions CI workflow

## 📁 Project Structure

```text
docker-task-manager/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
│
├── tests/
│   └── test_app.py
│
├── nginx/
│   └── default.conf
│
├── scripts/
│   └── backup.sh
│
├── backups/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
├── .env.example
└── README.md
```

## ⚙️ Requirements

Before running this project, install:

- Docker
- Docker Compose
- Git

## 🔧 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/SaeedMohsin/docker-task-manager.git
```

### 2. Open the project directory

```bash
cd docker-task-manager
```

### 3. Configure environment variables

Create your local environment file:

```bash
cp .env.example .env
```

Edit `.env` and configure your database credentials.

Do not upload your actual `.env` file to GitHub.

### 4. Create the Docker volume

```bash
docker volume create taskmanager_data
```

### 5. Build and start the containers

```bash
docker compose up -d --build
```

### 6. Check container status

```bash
docker compose ps
```

### 7. Open the application

```text
http://localhost:8080
```

## 🔌 API Endpoints

Base URL:

```text
http://localhost:8080
```

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application information |
| GET | `/health` | Application and database health |
| GET | `/api/tasks` | Retrieve all tasks |
| POST | `/api/tasks` | Create a new task |
| PUT | `/api/tasks/<id>` | Update a task |
| DELETE | `/api/tasks/<id>` | Delete a task |

## 🧪 API Examples

### Create a task

```bash
curl -X POST http://localhost:8080/api/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Learn Docker"}'
```

### Retrieve all tasks

```bash
curl http://localhost:8080/api/tasks
```

### Update a task

```bash
curl -X PUT http://localhost:8080/api/tasks/1 \
-H "Content-Type: application/json" \
-d '{"title":"Learn DevOps","completed":true}'
```

### Delete a task

```bash
curl -X DELETE http://localhost:8080/api/tasks/1
```

## 💾 Database Backup

The project includes a Bash script for PostgreSQL backups.

Run:

```bash
./scripts/backup.sh
```

Backup files are stored in the `backups/` directory.

## 🧪 Run Automated Tests

Activate the Python virtual environment and install dependencies:

```bash
pip install -r app/requirements.txt
```

Run:

```bash
python -m pytest -v
```

## 🔄 GitHub Actions

The GitHub Actions workflow automatically:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Runs automated tests.
5. Builds the Docker image.

Workflow file:

```text
.github/workflows/ci.yml
```

## 🛑 Stop the Application

```bash
docker compose down
```

The PostgreSQL data volume is preserved when containers are stopped this way.

**Important:** Avoid `docker compose down -v` if you want to preserve the database volume.

## 🎯 Learning Outcomes

Through this project, I practiced:

- Building and managing Docker containers.
- Creating multi-container applications with Docker Compose.
- Connecting Flask applications with PostgreSQL.
- Configuring Nginx as a reverse proxy.
- Managing Docker networks and volumes.
- Implementing health checks.
- Automating database backups using Bash.
- Writing automated tests with Pytest.
- Implementing CI using GitHub Actions.

## 👨‍💻 Author

**Saeed Mohsin**

BS Computer Science  
DevOps Learner

GitHub: [SaeedMohsin](https://github.com/SaeedMohsin)
