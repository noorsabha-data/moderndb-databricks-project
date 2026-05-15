# Databricks Workflow Configuration (Simple Demo Pipeline)

## Overview
This document describes a simple Databricks Workflow created using **:contentReference[oaicite:0]{index=0} Workflows (Jobs)**.

The goal of this workflow is to demonstrate basic orchestration by running two simple notebooks in sequence:
- Notebook 1: Prints "Hello World"
- Notebook 2: Prints "How are you"

This setup is used for learning and understanding job orchestration in Databricks.

---

## Workflow Name
simple-demo-workflow

---

## Cluster Configuration

- Cluster Type: Job Cluster
- Runtime: Databricks Runtime (DBR) 12.x or above
- Mode: Single Node (for simplicity)
- Auto Termination: Enabled (recommended)

---

## Tasks in Workflow

### Task 1: Hello World Notebook
- Notebook Name: `04_workflow_demo_1.py`
- Purpose:
  - Basic execution test
  - Prints a simple "Hello World" message
- Dependency: None (this is the first task)

**Example Output:**
Hello World

---

### Task 2: Greeting Notebook
- Notebook Name: `05_workflow_demo_2.py`
- Purpose:
  - Demonstrates sequential execution
  - Prints a simple greeting message
- Dependency:
  - Runs only after Task 1 succeeds

**Example Output:**
How are you

---

## Workflow Execution Flow
notebook1 (Hello World)
↓
notebook2 (How are you)


---

## Trigger Configuration

### Manual Trigger
- Workflow is executed manually from Databricks UI
- Used for testing and learning purposes

---

## Monitoring

- Execution status can be tracked in Databricks Job Runs UI
- Each task shows:
  - Start time
  - End time
  - Success/Failure status
- Logs can be viewed per notebook

---

## Key Learning Outcomes

This simple workflow demonstrates:

- Basic job orchestration in Databricks
- Sequential task execution using dependencies
- Notebook-based pipeline structure
- How workflows are managed in a Lakehouse environment

---

## Summary
This is a beginner-level Databricks workflow used to understand how multiple notebooks can be connected using Jobs. It forms the foundation for building more complex data pipelines in a Lakehouse architecture.