# DevOps Todo Project

This is a complete DevOps project demonstrating a full pipeline for a Python Flask web application.

[**View Repository on GitHub**](https://github.com/DEVENDRA4774/DevOps-Todo-Web-App)

## Tool Stack
- **Git & GitHub**: Version Control
- **GitHub Actions**: CI/CD Pipeline
- **Docker**: Containerization
- **Terraform**: Infrastructure as Code (IaC)
- **Ansible**: Configuration Management
- **Prometheus & Grafana**: Monitoring & Metrics

## Project Structure
```text
devops-todo-project/
├── app/
│   ├── app.py          (Flask app)
│   ├── templates/      (HTML templates)
│   ├── tests/          (Pytest tests)
│   └── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── terraform/
│   └── main.tf
├── ansible/
│   ├── playbook.yml
│   └── inventory
├── monitoring/
│   ├── prometheus.yml
│   └── grafana/
└── README.md
```

## Getting Started
1. Install dependencies: `pip install -r app/requirements.txt`
2. Run locally: `python app/app.py`
3. Visit `http://localhost:5000`
