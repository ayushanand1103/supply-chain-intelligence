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
