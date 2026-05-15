# Azure Access Connector Setup for Databricks

## Overview
The Access Connector enables secure authentication between Azure Databricks and Azure Data Lake Storage Gen2 using Managed Identity.

---

## Steps Performed

### 1. Create Access Connector
- Created an Azure Access Connector for Databricks in Azure Portal
- Selected system-assigned managed identity

---

### 2. Role Assignment
Assigned the following roles to the managed identity:

- Storage Blob Data Contributor
- Storage Blob Data Reader

Scope:
- Azure Data Lake Storage Gen2 account

---

### 3. Purpose
- Eliminates need for secrets or access keys
- Enables secure, identity-based access to storage

---

## Benefits
- No credential management required
- Secure authentication using Azure AD
- Production-grade security best practice