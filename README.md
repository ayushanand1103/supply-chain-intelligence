# National Supply Chain Intelligence Platform

An enterprise-grade **supply chain intelligence and forecasting system** inspired by large-scale operational platforms such as Palantir Gotham and Foundry.

This project focuses on building a **data-driven operational intelligence backbone** for supply chain systems, combining backend engineering, analytics, forecasting models, and scalable API infrastructure.

Unlike chatbot-based AI projects, this system is designed as a **real operational platform**, where AI/ML components enhance decision-making rather than act as the core system.

---

# 🧭 Overview

The platform provides centralized visibility and intelligence across:

- Warehouses
- Shipments
- Inventory
- Suppliers
- Logistics routes
- Operational risks
- Forecasting and ETA prediction

It enables organizations to monitor, analyze, and predict supply chain behavior in real time.

---

# 🚀 Core Features

## ✅ Current Features

### Backend & Infrastructure
- FastAPI backend (modular architecture)
- PostgreSQL integration
- SQLAlchemy ORM
- Pydantic validation
- RESTful API design
- Swagger/OpenAPI documentation

### Logistics System
- Warehouse management system
- Shipment lifecycle tracking
- Inventory tracking and updates
- CSV-based data ingestion pipeline

### Route Intelligence
- OSRM-based route calculation
- Distance and travel time estimation
- Geolocation-based warehouse system

### ETA Intelligence Engine (NEW)
- Moving Average smoothing model
- Exponential Smoothing model
- Kalman Filter real-time estimator
- Ensemble-based ETA prediction system
- Dynamic shipment time estimation

---

## 🔮 Planned Features

### Data Integration Layer
- Streaming ingestion pipelines
- External API integrations
- Live operational data sync

### Analytics Layer
- KPI dashboards (delays, throughput, efficiency)
- Risk scoring engine
- Trend and anomaly detection

### Forecasting System
- Demand forecasting
- Shipment delay prediction
- Inventory forecasting
- Time-series modeling (ARIMA, Prophet)

### Graph Intelligence Layer
- Supply chain dependency graphs
- Network optimization using Neo4j
- Route and node impact analysis

### AI Copilot (Future)
- Natural language queries on operations
- AI-generated insights
- Decision support assistant

---

# 🧠 ETA Intelligence System

The platform includes a real-time **multi-model ETA prediction engine**:

### Models used:
- Moving Average (noise reduction)
- Exponential Smoothing (trend adaptation)
- Kalman Filter (real-time correction)

### Output:
- Base OSRM ETA
- Smoothed ETA
- Final ensemble ETA

This enables **adaptive shipment time prediction** instead of static estimates.

---

# 🏗 System Architecture
Frontend Dashboard
↓
FastAPI Backend
↓
Business Logic Layer
↓
ETA + Analytics Engine
↓
SQLAlchemy ORM
↓
PostgreSQL Database

### Future Architecture


Data Sources
↓
Integration Layer (APIs + Streaming)
↓
Operational Database
↓
Analytics + Forecasting Engine
↓
Graph Intelligence Layer (Neo4j)
↓
Dashboards + Alerting System
↓
AI Copilot Layer


---

# 🛠 Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

## Database
- PostgreSQL

## Data Processing
- Pandas
- NumPy

## Machine Learning
- Moving Average Models
- Exponential Smoothing
- Kalman Filters
- (Future: ARIMA, Prophet, River ML)

## Frontend (Planned)
- React
- Tailwind CSS
- Recharts
- Axios

## Future Infrastructure
- Neo4j (Graph DB)
- Kafka (Streaming)
- Docker
- LangChain (AI Copilot)

---

# 📁 Project Structure


supply-chain-intelligence/
│
├── backend/
│ ├── app/
│ │ ├── models/
│ │ ├── routes/
│ │ ├── schemas/
│ │ ├── services/
│ │ ├── ml/
│ │ ├── integrations/
│ │ ├── utils/
│ │ ├── database.py
│ │ └── main.py
│ │
│ ├── requirements.txt
│ └── .env
│
├── frontend/
├── docs/
└── README.md


---

# ⚙️ Setup Instructions

## Clone Repository
```bash
git clone <repository-url>
cd supply-chain-intelligence
Backend Setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
PostgreSQL Setup
CREATE DATABASE supply_chain_db;
CREATE USER supply_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE supply_chain_db TO supply_user;
Run Backend
uvicorn app.main:app --reload
API: http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/docs
🧪 Current API Modules
Warehouses
Create warehouse
List warehouses
Shipments
Create shipment
Auto distance calculation (OSRM)
ETA prediction (ML ensemble system)
Inventory
Stock tracking
Auto updates on shipment creation
🧭 Development Roadmap
Phase 1 — Foundation
Backend architecture
Database design
Core CRUD APIs
CSV ingestion pipeline
Phase 2 — Operational Intelligence
Shipments system
Inventory intelligence
ETA prediction engine
Route optimization
Phase 3 — Forecasting & Analytics
Delay prediction models
Demand forecasting
Risk scoring engine
KPI dashboards
Phase 4 — Advanced Intelligence System
Graph-based supply chain modeling (Neo4j)
Real-time streaming (Kafka)
Alerting system
AI Copilot (natural language interface)
🎯 Project Goal

This project simulates a real-world enterprise supply chain intelligence system with:

Scalable backend architecture
Real-time operational analytics
Forecasting and prediction systems
ML-powered decision support
Modular system design
👨‍💻 Author

Ayush Anand
BSc Data Science & AI
Christ University, Delhi NCR



