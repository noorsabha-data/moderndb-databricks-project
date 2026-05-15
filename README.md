# Azure Databricks Lakehouse Pipeline (Delta + Auto Loader + Unity Catalog)

## 📌 Overview

This project demonstrates a modern **Azure Databricks Lakehouse architecture** using:

- Delta Lake (ACID transactions, versioning, time travel)
- Auto Loader (incremental streaming ingestion)
- Azure Data Lake Storage Gen2 (ADLS)
- Unity Catalog (governance & metadata management)
- Databricks Workflows (pipeline orchestration)

---

## 🏗️ Architecture

The pipeline follows a simple Lakehouse design:

1. Data ingestion using Auto Loader
2. Storage in ADLS Gen2
3. Transformation using Delta Lake
4. Governance using Unity Catalog
5. Orchestration using Databricks Workflows

---

## 🔧 Azure & Databricks Setup

### 1. Access Connector
- Enables secure connection between Databricks and ADLS
- Uses Managed Identity (no secrets required)

### 2. Unity Catalog Metastore
- Central metadata management layer
- Governs all tables and storage access

### 3. External Location
- Maps ADLS Gen2 storage to Databricks
- Enables secure external table creation

---

## ⚙️ Workflow Design

Databricks Workflows were used to simulate pipeline orchestration:

### Tasks:
- Task 1 → Auto Loader ingestion notebook
- Task 2 → Delta processing notebook
- Task 3 → Workflow execution demo notebook

---

## 📥 Auto Loader (Streaming Ingestion)

- Reads files incrementally from ADLS Gen2
- Automatically detects new files
- Maintains schema evolution using schemaLocation

---

## 🧱 Delta Lake Features Used

- ACID transactions
- UPDATE / INSERT operations
- Time travel (DESCRIBE HISTORY / RESTORE)
- OPTIMIZE for performance
- Deep Clone vs Shallow Clone

---

## 🔐 Security & Governance

Implemented using:
- Azure Access Connector
- Unity Catalog Metastore
- External Locations with controlled access

---

## 🚀 Key Learnings

- Built end-to-end Lakehouse pipeline
- Understood Databricks workflow orchestration
- Implemented secure Azure integration
- Worked with Delta Lake versioning and optimization

---

## 🛠️ Tech Stack

- Azure Databricks
- Azure Data Lake Storage Gen2
- Delta Lake
- PySpark
- Unity Catalog
- Databricks Workflows

---

## 📊 Future Improvements

- Add Medallion Architecture (Bronze/Silver/Gold)
- Replace demo notebooks with real datasets
- Add CI/CD for Databricks jobs
- Add monitoring and logging layer

---

## 👤 Author
**Noorsabha Qureshi**

Built by a Data Engineering learner exploring modern Lakehouse architecture on Azure Databricks.