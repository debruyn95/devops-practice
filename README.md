#  DevOps Monitoring Project

##  Overview
This project demonstrates a complete DevOps workflow by building, containerising, automating, and deploying a Python-based system monitoring application.

##  Tech Stack
- Python (psutil)
- Docker
- Git & GitHub
- GitHub Actions (CI/CD)
- AWS EC2 (Cloud Deployment)

## Features
- Monitors CPU, memory, and disk usage
- Runs continuously in real-time
- Containerised using Docker
- Automated build pipeline with GitHub Actions
- Deployed on AWS EC2 instance

##  DevOps Pipeline
Code → Git → GitHub → CI/CD → Docker → AWS EC2

## ▶ How to Run Locally
```bash
pip install psutil
python monitor.py
