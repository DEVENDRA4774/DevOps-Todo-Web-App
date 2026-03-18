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
## Project Diagrams

### 1. Deployment Diagram (The "DevOps" View)
This diagram illustrates the containerized deployment environment on the Docker host.

```mermaid
graph TD
    subgraph "Docker Host"
        subgraph "Network: bridge"
            WebApp["Todo Web App<br/>(Flask)"]
            Prometheus["Prometheus Server"]
            Grafana["Grafana Dashboard"]
        end
    end

    User((User)) -->|Port 5000| WebApp
    User -->|Port 3000| Grafana
    WebApp -->|Metrics Export| Prometheus
    Prometheus -->|Scrape /metrics| WebApp
    Grafana -->|Query Data| Prometheus
```

### 2. Component Diagram (The "Architecture" View)
This view shows the internal logic and integration points between the application and the monitoring stack.

```mermaid
C4Component
    title Component Diagram - DevOps Todo Web App

    Container_Boundary(api, "Todo Web App") {
        Component(ui, "Web UI", "HTML/Jinja2", "Frontend interface for managing tasks")
        Component(logic, "Flask API", "Python/Flask", "Handles CRUD operations for Todo list")
        Component(metrics, "Prometheus Client", "Python Library", "Exposes application metrics")
    }

    Container(prom, "Prometheus", "Service", "Time-series database for metrics")
    Container(graf, "Grafana", "Service", "Visualization dashboard")

    Rel(ui, logic, "Uses", "HTTP")
    Rel(logic, metrics, "Instruments")
    Rel(prom, metrics, "Scrapes metrics from", "HTTP/metrics")
    Rel(graf, prom, "Queries data from")
```

### 3. Sequence Diagram (The "Process" View)
This diagram traces the flow of a user interaction and how it is observed by the monitoring system.

```mermaid
sequenceDiagram
    participant User
    participant WebApp as Todo Web App
    participant Prom as Prometheus
    participant Graf as Grafana

    User->>WebApp: Create Task (POST /)
    WebApp->>WebApp: Update In-Memory Task List
    WebApp->>WebApp: Increment 'tasks_created' metric
    WebApp-->>User: 200 OK (Render Index)

    Note over Prom, WebApp: Asynchronous Scraping
    Prom->>WebApp: GET /metrics
    WebApp-->>Prom: tasks_created_total{...} 10
    
    Note over Graf, Prom: Real-time Visualization
    Graf->>Prom: Query metric values
    Prom-->>Graf: Data points
    Graf->>User: Update Dashboard Visualization
```
