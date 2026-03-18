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
    subgraph Host ["Docker Host (Linux)"]
        subgraph Net ["Network: bridge"]
            WebApp["Todo Web App<br/>(Flask:5000)"]
            Prometheus["Prometheus Server<br/>(Monitoring:9090)"]
            Grafana["Grafana Dashboard<br/>(Visuals:3000)"]
        end
    end

    User((User)) -->|Access| WebApp
    User -->|View| Grafana
    WebApp -- "Metrics" --> Prometheus
    Prometheus -- "Scrape" --> WebApp
    Grafana -- "Query" --> Prometheus

    style Host fill:#222,stroke:#666,stroke-width:2px,color:#fff
    style Net fill:#333,stroke:#666,stroke-dasharray: 5 5,color:#fff
    style WebApp fill:#1f77b4,stroke:#fff,stroke-width:2px,color:#fff
    style Prometheus fill:#ff7f0e,stroke:#fff,stroke-width:2px,color:#fff
    style Grafana fill:#d62728,stroke:#fff,stroke-width:2px,color:#fff
    style User fill:#2ca02c,stroke:#fff,stroke-width:2px,color:#fff
```

### 2. Component Diagram (The "Architecture" View)
This view shows the internal logic and integration points between the application and the monitoring stack.

```mermaid
graph TB
    subgraph App ["Todo Web App (Flask)"]
        UI["Web UI<br/>(HTML/Jinja2)"]
        Logic["Flask API<br/>(Business Logic)"]
        Client["Prometheus Client<br/>(Instrumentation)"]
        
        UI --- Logic
        Logic --- Client
    end

    Prom["Prometheus Server<br/>(Metrics DB)"]
    Graf["Grafana Dashboard<br/>(Visualization)"]

    Logic -- "1. Exposes /metrics" --> Client
    Prom -- "2. Scrapes Data" --> Client
    Graf -- "3. Queries" --> Prom
    
    style App fill:#333,stroke:#666,stroke-width:2px,color:#fff
    style UI fill:#1f77b4,stroke:#fff,stroke-width:2px,color:#fff
    style Logic fill:#1f77b4,stroke:#fff,stroke-width:2px,color:#fff
    style Client fill:#1f77b4,stroke:#fff,stroke-width:2px,color:#fff
    style Prom fill:#ff7f0e,stroke:#fff,stroke-width:2px,color:#fff
    style Graf fill:#d62728,stroke:#fff,stroke-width:2px,color:#fff
```

### 3. Sequence Diagram (The "Process" View)
This diagram traces the flow of a user interaction and how it is observed by the monitoring system.

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant W as Todo Web App
    participant P as Prometheus
    participant G as Grafana

    Note over U, G: Request & Metric Flow

    U->>W: Create Task (POST /)
    W->>W: Update In-Memory List
    W->>W: Incr 'tasks_created'
    W-->>U: Render Index Page

    rect rgb(40, 40, 40)
        Note right of P: Scrape Interval
        P->>W: GET /metrics
        W-->>P: task_total 1
    end

    rect rgb(50, 50, 50)
        Note left of G: UI Refresh
        G->>P: Query Metrics
        P-->>G: Data Points
        G->>U: Update Dashboard
    end
```
