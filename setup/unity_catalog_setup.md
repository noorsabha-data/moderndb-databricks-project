# Unity Catalog Setup in Databricks

## Overview
Unity Catalog is the central governance layer in Databricks that provides fine-grained access control, data lineage, and centralized metadata management.

---

## Steps Performed

### 1. Metastore Creation
- Created a Unity Catalog Metastore in Databricks Account Console
- Assigned it to the Azure Databricks workspace

---

### 2. Workspace Assignment
- Linked the workspace to the created metastore
- Enabled Unity Catalog as the default governance layer

---

### 3. Catalog and Schema Creation
```sql
CREATE CATALOG man_cata;

CREATE SCHEMA man_cata.man_schema;

```

---
### 4. Benefits Achieved
- Centralized metadata management
- Fine-grained access control (table/column level)
- Data lineage tracking
- Secure data sharing across workspaces