# National Supply Chain Intelligence Platform

An enterprise-style operational intelligence platform inspired by systems like Palantir Gotham and Foundry.

This project integrates operational data from multiple sources, performs analytics and forecasting, and provides centralized dashboards for monitoring supply chain operations.

---

# Overview

The platform is designed for organizations that need visibility into:

* Warehouses
* Shipments
* Inventory
* Suppliers
* Operational risks
* Forecasting and analytics

Instead of building a simple LLM wrapper or chatbot application, this project focuses on:

* Backend architecture
* Data engineering
* Operational analytics
* Forecasting systems
* Enterprise workflows
* API-driven infrastructure

The AI/LLM layer is optional and acts as a supporting intelligence interface rather than the core system.

---

# Core Features

## Current Features

* FastAPI backend
* PostgreSQL integration
* SQLAlchemy ORM
* Warehouse APIs
* Pydantic validation
* REST API architecture
* Swagger/OpenAPI documentation

---

## Planned Features

### Data Integration

* CSV uploads
* API ingestion
* Operational data pipelines

### Supply Chain Management

* Warehouse monitoring
* Shipment tracking
* Supplier management
* Inventory monitoring

### Analytics

* KPI dashboards
* Delay analysis
* Risk scoring
* Trend analysis

### Forecasting

* Demand forecasting
* Inventory forecasting
* Shipment delay prediction
* Anomaly detection

### Graph Intelligence

* Supply chain relationship mapping
* Dependency analysis
* Network visualization using Neo4j

### AI Copilot (Future)

* Natural language operational queries
* AI-generated operational insights
* Conversational analytics assistant

---

# System Architecture

```text
Frontend Dashboard
        ↓
FastAPI Backend
        ↓
Business Logic Layer
        ↓
SQLAlchemy ORM
        ↓
PostgreSQL Database
```

Future architecture:

```text
Data Sources
      ↓
Integration Layer
      ↓
Operational Database
      ↓
Analytics + Forecasting
      ↓
Graph Intelligence
      ↓
Dashboards + Alerts
      ↓
AI Copilot
```

---

# Tech Stack

## Frontend

* React
* Tailwind CSS
* Recharts
* Axios

## Backend

* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

## Database

* PostgreSQL

## Machine Learning

* Pandas
* Scikit-learn
* Prophet

## Future Technologies

* Neo4j
* Kafka
* Docker
* LangChain

---

# Project Structure

```text
supply-chain-intelligence/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── database.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
├── docs/
└── README.md
```

---

# Backend Setup

## Clone Repository

```bash
git clone <repository-url>
cd supply-chain-intelligence
```

---

## Create Virtual Environment

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Install PostgreSQL:

```bash
sudo apt install postgresql postgresql-contrib -y
```

Start PostgreSQL:

```bash
sudo service postgresql start
```

Open PostgreSQL shell:

```bash
sudo -u postgres psql
```

Create database:

```sql
CREATE DATABASE supply_chain_db;
```

Create user:

```sql
CREATE USER supply_user WITH PASSWORD 'password';
```

Grant permissions:

```sql
GRANT ALL PRIVILEGES ON DATABASE supply_chain_db TO supply_user;
GRANT ALL ON SCHEMA public TO supply_user;
ALTER SCHEMA public OWNER TO supply_user;
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Existing API Endpoints

## Warehouse APIs

### Create Warehouse

```http
POST /warehouses/
```

Example:

```json
{
  "name": "Delhi Central Warehouse",
  "city": "Delhi",
  "capacity": 5000
}
```

---

### Get Warehouses

```http
GET /warehouses/
```

---

# Development Roadmap

## Phase 1 — Foundation

* Backend setup
* PostgreSQL integration
* CRUD APIs
* Frontend dashboard

## Phase 2 — Operational Intelligence

* Shipments module
* Supplier module
* Inventory module
* KPI analytics

## Phase 3 — Forecasting

* Demand forecasting
* Delay prediction
* Risk scoring
* Anomaly detection

## Phase 4 — Advanced Intelligence

* Neo4j graph relationships
* Real-time streaming
* Operational alerts
* AI copilot

---

# Goals of the Project

This project aims to simulate how modern enterprise intelligence systems operate.

The focus is on:

* Scalable architecture
* Data-driven operations
* Operational visibility
* Forecasting systems
* Enterprise backend engineering

---

# Author

Ayush Anand
BSc Data Science & AI
Christ University Delhi NCR
