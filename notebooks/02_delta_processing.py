{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "1755b00c-405a-427a-a5c7-159740975389",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Delta Table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778795116272,
     "inputWidgets": {},
     "nuid": "24360a75-f10d-4e4f-8ebf-1d7cf74d4672",
     "showTitle": false,
     "startTime": 1778795097593,
     "submitTime": 1778795097237,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE TABLE man_cata.man_schema.deltatbl\n",
    "(\n",
    "    id INT,\n",
    "    name STRING,\n",
    "    city STRING\n",
    ")\n",
    "USING DELTA\n",
    "LOCATION 'abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/deltalake/deltatbl'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "ad155763-695c-4d4e-aae4-f8be7f07ae5b",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "### Turning off Deletion vector\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778795213497,
     "inputWidgets": {},
     "nuid": "2afe5cae-2663-4076-bfa0-07044df480c0",
     "showTitle": false,
     "startTime": 1778795211720,
     "submitTime": 1778795211662,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "ALTER TABLE man_cata.man_schema.deltatbl\n",
    "SET TBLPROPERTIES (\n",
    "  'delta.enableDeletionVectors' = false\n",
    ");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778795489213,
     "inputWidgets": {},
     "nuid": "a9ed2b69-e681-48f6-8926-bc523b32719c",
     "showTitle": false,
     "startTime": 1778795481123,
     "submitTime": 1778795481048,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "INSERT INTO man_cata.man_schema.deltatbl\n",
    "VALUES\n",
    "(1, 'John', 'New York'),\n",
    "(2, 'Jane', 'Los Angeles'),\n",
    "(3, 'Bob', 'Chicago'),\n",
    "(4, 'Alice', 'Houston');\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778799025154,
     "inputWidgets": {},
     "nuid": "a4afa0c9-fdaa-4f0f-9d4f-1ff8e9e6c0e4",
     "showTitle": false,
     "startTime": 1778799023130,
     "submitTime": 1778799023061,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM man_cata.man_schema.deltatbl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778795551381,
     "inputWidgets": {},
     "nuid": "5d3af0bd-7478-4c1d-85ca-468eecf27a7c",
     "showTitle": false,
     "startTime": 1778795549894,
     "submitTime": 1778795549843,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "DESCRIBE EXTENDED man_cata.man_schema.deltatbl"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "874d0ddb-15d7-4402-a52b-b3b000c44b75",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**UPDATES IN DELTA TABLE**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778798922211,
     "inputWidgets": {},
     "nuid": "a95e8f44-8bb0-4787-8f3d-a0281bf8d5cf",
     "showTitle": false,
     "startTime": 1778798900324,
     "submitTime": 1778798900228,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "UPDATE man_cata.man_schema.deltatbl\n",
    "SET name = 'Mary'\n",
    "WHERE id = 1;"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "d6e28e84-742e-464e-b0d7-1a6df55b00f3",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Versioning**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778798956040,
     "inputWidgets": {},
     "nuid": "aaecf832-7617-49cf-b280-6119f9a30708",
     "showTitle": false,
     "startTime": 1778798952918,
     "submitTime": 1778798952847,
     "tableResultSettingsMap": {
      "0": {
       "dataGridStateBlob": "{\"version\":1,\"tableState\":{\"columnPinning\":{\"left\":[\"#row_number#\"],\"right\":[]},\"columnSizing\":{\"operation\":142},\"columnVisibility\":{}},\"settings\":{\"columns\":{}},\"syncTimestamp\":1778798970498}",
       "filterBlob": null,
       "queryPlanFiltersBlob": null,
       "tableResultIndex": 0
      }
     },
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "DESCRIBE HISTORY man_cata.man_schema.deltatbl"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "d4985780-e24b-445b-b1a4-ae6b16c1e983",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Time Travel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778799218988,
     "inputWidgets": {},
     "nuid": "f421dd62-bf62-47ba-8672-6704e4fbbd8d",
     "showTitle": false,
     "startTime": 1778799197012,
     "submitTime": 1778799196946,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "RESTORE man_cata.man_schema.deltatbl TO VERSION AS OF 2;\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778799245310,
     "inputWidgets": {},
     "nuid": "1badb94c-32a2-4029-abe3-4c2f618b44d9",
     "showTitle": false,
     "startTime": 1778799243627,
     "submitTime": 1778799243596,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM man_cata.man_schema.deltatbl"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "e237707e-b728-4bd0-9810-5066cec288b5",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Lets create another table to learn deletion vector**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778799699033,
     "inputWidgets": {},
     "nuid": "b6c97f9a-0013-4cda-894b-5290eaa4fbd3",
     "showTitle": false,
     "startTime": 1778799696629,
     "submitTime": 1778799696584,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE TABLE man_cata.man_schema.deltatbl_1\n",
    "(\n",
    "    id INT,\n",
    "    name STRING,\n",
    "    city STRING\n",
    ")\n",
    "USING DELTA\n",
    "LOCATION 'abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/deltalake/deltatbl_1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778799763115,
     "inputWidgets": {},
     "nuid": "6230cd51-a8f7-46a7-85d8-9903affde2ae",
     "showTitle": false,
     "startTime": 1778799761089,
     "submitTime": 1778799761001,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "INSERT INTO man_cata.man_schema.deltatbl_1\n",
    "VALUES\n",
    "(1, 'John', 'New York'),\n",
    "(2, 'Jane', 'Los Angeles'),\n",
    "(3, 'Bob', 'Chicago'),\n",
    "(4, 'Alice', 'Houston');\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "0ce49c8b-9b86-4ff6-baae-9433faa949c4",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**checking wheather deletion vector is on or no**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778799788242,
     "inputWidgets": {},
     "nuid": "e7e85a0d-fe1b-4cee-8fa2-690c8d598e81",
     "showTitle": false,
     "startTime": 1778799787282,
     "submitTime": 1778799787235,
     "tableResultSettingsMap": {
      "0": {
       "dataGridStateBlob": "{\"version\":1,\"tableState\":{\"columnPinning\":{\"left\":[\"#row_number#\"],\"right\":[]},\"columnSizing\":{\"tableFeatures\":336},\"columnVisibility\":{}},\"settings\":{\"columns\":{}},\"syncTimestamp\":1778799808721}",
       "filterBlob": null,
       "queryPlanFiltersBlob": null,
       "tableResultIndex": 0
      }
     },
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "DESCRIBE DETAIL man_cata.man_schema.deltatbl_1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778800193667,
     "inputWidgets": {},
     "nuid": "9970a378-8913-4e82-bf3e-d2b1d5bbd3ca",
     "showTitle": false,
     "startTime": 1778800189399,
     "submitTime": 1778800189336,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "UPDATE man_cata.man_schema.deltatbl_1\n",
    "SET name = 'Mary'\n",
    "WHERE id = 1;"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "d16debc1-8ef6-416c-9ecb-3a58525640b6",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "#### Optimization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778802543091,
     "inputWidgets": {},
     "nuid": "5de49f5c-d67b-4742-92ca-e486961ea8d7",
     "showTitle": false,
     "startTime": 1778802535898,
     "submitTime": 1778802535796,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "DESCRIBE HISTORY man_cata.man_schema.deltatbl_1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778802582026,
     "inputWidgets": {},
     "nuid": "c329442b-8a4e-4f11-a02c-3dcfdccaca5a",
     "showTitle": false,
     "startTime": 1778802576919,
     "submitTime": 1778802576874,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "OPTIMIZE man_cata.man_schema.deltatbl_1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "7f076af8-374c-48db-b4be-cf7345982aa0",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Deep clone vs shallow clone**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "ebc619c2-3d1f-4a79-8251-3bbd464dea63",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Deep Copy**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778827320784,
     "inputWidgets": {},
     "nuid": "9f5231c8-8de0-4a1b-998b-805b1aa2e5a4",
     "showTitle": false,
     "startTime": 1778827268090,
     "submitTime": 1778826869342,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE TABLE man_cata.man_schema.deepclonetbl\n",
    "DEEP CLONE man_cata.man_schema.deltatbl;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778827469549,
     "inputWidgets": {},
     "nuid": "26425963-3758-46ee-8d6d-1d4790deb4b8",
     "showTitle": false,
     "startTime": 1778827465729,
     "submitTime": 1778827465635,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM man_cata.man_schema.deepclonetbl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778827484876,
     "inputWidgets": {},
     "nuid": "622cf5ae-aa0b-40c6-878b-f4d0fa6c62b5",
     "showTitle": false,
     "startTime": 1778827483040,
     "submitTime": 1778827482997,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM man_cata.man_schema.deltatbl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778827512915,
     "inputWidgets": {},
     "nuid": "7aac3bf5-c0bc-4c34-8b83-19e65621d1fa",
     "showTitle": false,
     "startTime": 1778827504142,
     "submitTime": 1778827504093,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "UPDATE man_cata.man_schema.deltatbl\n",
    "SET city = 'Toronto' WHERE id=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778827527055,
     "inputWidgets": {},
     "nuid": "1a67d0ca-6359-4709-a048-4be6c08feb83",
     "showTitle": false,
     "startTime": 1778827525555,
     "submitTime": 1778827525509,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM man_cata.man_schema.deepclonetbl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778827520345,
     "inputWidgets": {},
     "nuid": "099a99b6-697a-4ba1-98eb-7718dc4fba4f",
     "showTitle": false,
     "startTime": 1778827518495,
     "submitTime": 1778827518454,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM man_cata.man_schema.deltatbl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778827534665,
     "inputWidgets": {},
     "nuid": "c19878fb-0d53-442a-ba61-4a310836be72",
     "showTitle": false,
     "startTime": 1778827531953,
     "submitTime": 1778827531889,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "DESCRIBE HISTORY man_cata.man_schema.deepclonetbl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778827572320,
     "inputWidgets": {},
     "nuid": "721b8b96-318b-468a-9ef8-4967a13a2ede",
     "showTitle": false,
     "startTime": 1778827568737,
     "submitTime": 1778827568696,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "DESCRIBE EXTENDED man_cata.man_schema.deepclonetbl"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "b98f5f2f-4442-4740-9fe2-e7dffb5e5b1f",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Shallow copy**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778828684129,
     "inputWidgets": {},
     "nuid": "ca8be99b-1d12-4db8-b33b-99772a84f765",
     "showTitle": false,
     "startTime": 1778828678096,
     "submitTime": 1778828678021,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE TABLE man_cata.man_schema.shallowcloneclonetbl\n",
    "SHALLOW CLONE man_cata.man_schema.man_table;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "finishTime": 1778830977565,
     "inputWidgets": {},
     "nuid": "8ad7d26a-fefd-4d4a-83d7-afcf2804b7bc",
     "showTitle": false,
     "startTime": 1778830945280,
     "submitTime": 1778830788678,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql \n",
    "DESCRIBE EXTENDED man_cata.man_schema.shallowcloneclonetbl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "b210d8e5-d557-45eb-a01f-4f78a9442e32",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "332a5150-513f-4b96-99ab-7fa5a25366bd",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "5"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": 5208317522993035,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "Delta_Tutorial",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
