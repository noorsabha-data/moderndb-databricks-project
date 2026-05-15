{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "c390f2ec-e169-4ad5-8ad5-0cb3c3a6b364",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "# My Magic Commands Practice\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1778708623779,
     "inputWidgets": {},
     "nuid": "c46e0e24-f2e0-4f64-a778-6a100e861e7f",
     "showTitle": false,
     "startTime": 1778708597761,
     "submitTime": 1778708505813,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%fs ls /\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1778708635215,
     "inputWidgets": {},
     "nuid": "06785c29-f53a-4b72-b55e-4657e188607c",
     "showTitle": false,
     "startTime": 1778708634962,
     "submitTime": 1778708634903,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sh\n",
    "echo \"Hello from shell\"\n",
    "python --version"
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
     "finishTime": 1778708654825,
     "inputWidgets": {},
     "nuid": "7254d87e-05bd-4973-918b-74bd891dec49",
     "showTitle": false,
     "startTime": 1778708651141,
     "submitTime": 1778708651100,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT current_date(), current_timestamp()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1778708665829,
     "inputWidgets": {},
     "nuid": "5d4af491-e6e8-4966-ad92-0901a806faef",
     "showTitle": false,
     "startTime": 1778708665557,
     "submitTime": 1778708665516,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%python\n",
    "print(\"Hello from Python\")\n",
    "spark.version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "8aea7819-9d0f-4521-860d-bb441b5a5400",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "df02d23d-0c72-493b-8f89-ae50a11679bb",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "### Scenario - 1\n",
    "**-Managed Catalog**\n",
    "**-Managed Schema**\n",
    "**-Managed Table**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "1ff5530a-6451-4596-83bd-066f43915cd5",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Managed Catalog**\n"
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
     "finishTime": 1778727908716,
     "inputWidgets": {},
     "nuid": "562357f4-e5c5-49e1-ba22-a0cfeb08c56b",
     "showTitle": false,
     "startTime": 1778727897621,
     "submitTime": 1778727561138,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE CATALOG man_cata"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "e1709588-136a-4aa2-bdb0-d417c9d6140e",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Managed Schema/Database**"
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
     "finishTime": 1778728012576,
     "inputWidgets": {},
     "nuid": "c7c1de8f-69a7-416d-a949-0188b9fb8b48",
     "showTitle": false,
     "startTime": 1778728011104,
     "submitTime": 1778728011012,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE SCHEMA man_cata.man_schema"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "7e05cff5-727a-44b3-b043-6cbb525521c7",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Managed Table**"
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
     "finishTime": 1778728189449,
     "inputWidgets": {},
     "nuid": "f0d143f1-fdc1-4555-96ef-6771d19e17bf",
     "showTitle": false,
     "startTime": 1778728180439,
     "submitTime": 1778728180347,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE TABLE man_cata.man_schema.man_table \n",
    "(id INT, \n",
    "name STRING\n",
    ")\n",
    "USING DELTA \n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "f568af12-5174-4ec0-8448-0c715716841b",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "### Scenario - 2\n",
    "**-External Catalog**\n",
    "**-Managed Schema**\n",
    "**-Managed Table**"
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
     "finishTime": 1778728504312,
     "inputWidgets": {},
     "nuid": "07e0da26-6376-47bb-903f-fe3aa09aa7b2",
     "showTitle": false,
     "startTime": 1778728502769,
     "submitTime": 1778728502704,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE CATALOG ext_cata"
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
     "finishTime": 1778728577010,
     "inputWidgets": {},
     "nuid": "532b1485-6b9e-48d8-a3e8-72ea7aff6524",
     "showTitle": false,
     "startTime": 1778728574764,
     "submitTime": 1778728574713,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "DROP CATALOG IF EXISTS ext_cata"
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
     "finishTime": 1778728872832,
     "inputWidgets": {},
     "nuid": "c273d381-b7b1-4832-a974-d54327f7205a",
     "showTitle": false,
     "startTime": 1778728872145,
     "submitTime": 1778728872108,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "DROP CATALOG IF EXISTS ext_cata CASCADE;"
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
     "finishTime": 1778728897753,
     "inputWidgets": {},
     "nuid": "ba59ba1f-7151-4359-8b31-34924e84b42b",
     "showTitle": false,
     "startTime": 1778728897138,
     "submitTime": 1778728897102,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE CATALOG IF NOT EXISTS ext_cata\n",
    "MANAGED LOCATION 'abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/external_catalog'"
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
     "finishTime": 1778729226637,
     "inputWidgets": {},
     "nuid": "4280a0d5-8541-4c7e-b103-82e995e3b32f",
     "showTitle": false,
     "startTime": 1778729225865,
     "submitTime": 1778729225789,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE SCHEMA ext_cata.man_schema"
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
     "finishTime": 1778729421315,
     "inputWidgets": {},
     "nuid": "df2df41d-7c21-4837-b489-4e91cbdd1b24",
     "showTitle": false,
     "startTime": 1778729419334,
     "submitTime": 1778729419269,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE TABLE ext_cata.man_schema.man_table2\n",
    "(id INT,\n",
    "name STRING\n",
    ")\n",
    "USING DELTA \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "563c8ff7-667a-4206-a535-300f87279491",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "### Scenario - 3\n",
    "**-External Catalog**\n",
    "**-External Schema**\n",
    "**-Managed Table**"
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
     "finishTime": 1778730018104,
     "inputWidgets": {},
     "nuid": "7f3af24c-6369-4fd8-b1ab-f55ed9011030",
     "showTitle": false,
     "startTime": 1778730017093,
     "submitTime": 1778730017009,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE SCHEMA ext_cata.ext_schema\n",
    "MANAGED LOCATION 'abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/external_schema'"
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
     "finishTime": 1778730064348,
     "inputWidgets": {},
     "nuid": "6341aae9-30f2-4de4-9f93-5eb9db0d8921",
     "showTitle": false,
     "startTime": 1778730062433,
     "submitTime": 1778730062400,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE TABLE ext_cata.ext_schema.man_table3\n",
    "(id INT,\n",
    "name STRING\n",
    ")\n",
    "USING DELTA "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "ccedde8d-a8f0-4811-b5bc-4b4bbab19de7",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "### Scenario - 4\n",
    "**-Managed Catalog**\n",
    "**-Managed Schema**\n",
    "**-External Table**"
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
     "finishTime": 1778730565156,
     "inputWidgets": {},
     "nuid": "7764da2d-d659-415c-a8e7-f0ca28696a9c",
     "showTitle": false,
     "startTime": 1778730562886,
     "submitTime": 1778730562738,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE TABLE man_cata.man_schema.ext_table\n",
    "(id INT,\n",
    "name STRING\n",
    ")\n",
    "USING DELTA\n",
    "LOCATION 'abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/external_table/man_table3'\n",
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
     "finishTime": 1778782166469,
     "inputWidgets": {},
     "nuid": "d98d80c6-c13d-4854-b9fa-8ee5e792e31a",
     "showTitle": false,
     "startTime": 1778782141082,
     "submitTime": 1778781801497,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "INSERT INTO man_cata.man_schema.ext_table\n",
    "VALUES \n",
    "(1,'John'),\n",
    "(2,'Mary'),\n",
    "(3,'Jane'),\n",
    "(4,'Bob'),\n",
    "(5,'Alice')\n",
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
     "finishTime": 1778782446802,
     "inputWidgets": {},
     "nuid": "a7f5ffba-68f2-4da1-8509-b0da8f363e2b",
     "showTitle": false,
     "startTime": 1778782440801,
     "submitTime": 1778782440567,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM man_cata.man_schema.ext_table"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "9ef6b643-be30-40dc-9fd0-1dca2ad1d085",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "### Drop Managed Table"
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
     "finishTime": 1778730976129,
     "inputWidgets": {},
     "nuid": "8618ce97-7485-4f82-84a8-1a98c6442efe",
     "showTitle": false,
     "startTime": 1778730975269,
     "submitTime": 1778730975208,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "DROP TABLE man_cata.man_schema.man_table;"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "8fbde0c3-5e64-4f91-be28-503cc150028f",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "### UNDrop Managed Table"
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
     "finishTime": 1778731076724,
     "inputWidgets": {},
     "nuid": "b46736a7-a504-43be-a8d5-098a88cdc311",
     "showTitle": false,
     "startTime": 1778731075978,
     "submitTime": 1778731075928,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "UNDROP TABLE man_cata.man_schema.man_table;"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "49e34549-4fb6-4f06-a20c-8c4624095316",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "### Querying Files Using SELECT"
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
     "finishTime": 1778783243713,
     "inputWidgets": {},
     "nuid": "fb5a2a1f-3384-4de5-b544-9b5112c6a916",
     "showTitle": false,
     "startTime": 1778783240869,
     "submitTime": 1778783240803,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM delta.`abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/external_table/man_table3`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "08d747a2-0638-4e17-b9db-ff96fb29a3ab",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## Permanent VIEWS"
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
     "finishTime": 1778784054581,
     "inputWidgets": {},
     "nuid": "222fab56-3808-473c-b4e1-2f87dccda465",
     "showTitle": false,
     "startTime": 1778784052814,
     "submitTime": 1778784052738,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE VIEW man_cata.man_schema.view1\n",
    "AS \n",
    "SELECT * FROM delta.`abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/external_table/man_table3` WHERE id=1"
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
     "finishTime": 1778784114034,
     "inputWidgets": {},
     "nuid": "3fb89b8d-7ac5-43de-b566-398365155346",
     "showTitle": false,
     "startTime": 1778784111507,
     "submitTime": 1778784111472,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM man_cata.man_schema.view1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "cd442dfd-9597-48b5-90d7-e7affe806f3f",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "##Temporary VIEWS"
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
     "finishTime": 1778784246939,
     "inputWidgets": {},
     "nuid": "f7405b6e-cf41-4cd7-bbbc-787febe22dd1",
     "showTitle": false,
     "startTime": 1778784245910,
     "submitTime": 1778784245844,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE OR REPLACE TEMP VIEW temp_view\n",
    "AS\n",
    "SELECT * FROM delta.`abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/external_table/man_table3` WHERE id=1\n",
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
     "finishTime": 1778784261452,
     "inputWidgets": {},
     "nuid": "e61f35e8-bd28-4f66-8c47-10f1898e4b33",
     "showTitle": false,
     "startTime": 1778784259623,
     "submitTime": 1778784259587,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM temp_view"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "2fad3d3f-1622-4675-96a4-8518d2962f58",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "##Volumes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "9cb6fefd-2bdb-40c1-b98c-48311a69b26a",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Creating a Directory For Volume**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1778787972313,
     "inputWidgets": {},
     "nuid": "f29cc76a-dd48-41fa-b4af-c38f08394bfa",
     "showTitle": false,
     "startTime": 1778787953109,
     "submitTime": 1778787560673,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "dbutils.fs.mkdirs('abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/volumes')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "fb937d08-f66e-4844-aa72-b10b5bb9b99d",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Creating a External Volume**"
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
     "finishTime": 1778788056540,
     "inputWidgets": {},
     "nuid": "4a6e9a87-b25e-4130-9c23-bb4ed04dc805",
     "showTitle": false,
     "startTime": 1778788054532,
     "submitTime": 1778788054432,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE EXTERNAL VOLUME man_cata.man_schema.extvolume\n",
    "LOCATION 'abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/volumes'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "8e2b462f-225e-45ce-9311-bdce67f1e3c5",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Copy. File For Volume**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1778788999452,
     "inputWidgets": {},
     "nuid": "5e632dfc-6073-4a4b-8e4e-032aba50c3fb",
     "showTitle": false,
     "startTime": 1778788998280,
     "submitTime": 1778788998227,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "dbutils.fs.cp('abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/source/bollywood.csv','abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/volumes/bollywood')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1778788300560,
     "inputWidgets": {},
     "nuid": "3478ccee-3926-4abe-9da9-6056177cf981",
     "showTitle": false,
     "startTime": 1778788299420,
     "submitTime": 1778788299289,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "dbutils.fs.ls(\"abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1778789788522,
     "inputWidgets": {},
     "nuid": "0b7cd44b-e89c-4910-9025-e2d87690fc4b",
     "showTitle": false,
     "startTime": 1778789787748,
     "submitTime": 1778789787672,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "dbutils.fs.ls(\"abfss://mycontainer@noorstoragemoderndb.dfs.core.windows.net/source/\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "c6f789ab-d319-4030-a7cb-9a741dca4d12",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "**Querying Volume**"
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
     "finishTime": 1778790066565,
     "inputWidgets": {},
     "nuid": "c4eec176-e8dc-42a0-b3f3-82bc5297df70",
     "showTitle": false,
     "startTime": 1778790054220,
     "submitTime": 1778790054182,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%sql\n",
    "SELECT * FROM `csv`.`/Volumes/man_cata/man_schema/extvolume/bollywood`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "351c8b63-de6f-4919-8482-203387cdbb37",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "67194700-2f3b-417a-bff2-b0b0a6e065e6",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": []
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": {
    "hardware": {
     "accelerator": null,
     "gpuPoolId": null,
     "memory": null
    },
    "software": {
     "pinSparkToX86": null
    }
   },
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "5"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": 5436552850497608,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "tutorial_1",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
