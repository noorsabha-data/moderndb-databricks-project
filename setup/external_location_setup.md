# External Location Setup in Unity Catalog

## Overview
External Locations map cloud storage (ADLS Gen2) to Databricks Unity Catalog for secure and governed data access.

---

## Steps Performed

### 1. Storage Path Registration
Registered ADLS Gen2 path: abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/

---

### 2. Create Storage Credential
Linked Access Connector identity as storage credential.

---

### 3. Create External Location
```sql
CREATE EXTERNAL LOCATION my_external_location
URL 'abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL my_storage_credential);
```

---

### 4. Grant Permissions
```sql
GRANT READ FILES, WRITE FILES
ON EXTERNAL LOCATION my_external_location
TO `account users`;
```

---

### Benefits
- Secure access to ADLS through Unity Catalog
- Centralized governance of storage paths
- Controlled data access without exposing credentials

---

# 🧠 How these 3 files work together (IMPORTANT)
> “Unity Catalog provides governance, Access Connector provides secure identity, and External Locations map cloud storage into Databricks in a controlled way.”

---



