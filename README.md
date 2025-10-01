# Test Data Engineer Mandiri Sekuritas - Luthfi Nabhan Ibrahim

📊 Mandiri Sekuritas Technical Test

This zip files contains solutions for the Mandiri Sekuritas Technical Test for task 1 -5:

Task 1: Complaint Resolution Analysis (static PDF report)

Task 2: Luxury Loan Portfolio Dashboard (interactive Plotly Dash app)

Task 3 - 5 : In answer3-5.txt

### Prerequisites For Task 1 - 2

* Docker
* Docker Compose
* Python
* Postgres


## 📦 Services

### 1. Database (`db`)
- **Image**: `postgres:15`
- **Container name**: `crm_postgres`
- **Database**: `crmdb`
- **User**: `admin`
- **Password**: `Test1234`
- **Ports**: `5432:5432`
- **Volumes**:
  - `./db/init:/docker-entrypoint-initdb.d` → initialization scripts
  - `./task1/data:/data` → additional data
  - `db_data:/var/lib/postgresql/data` → persistent database storage

### 2. Task1 (`task1`)
- **Container name**: `crm_task1`
- **Build**: `Dockerfile.task1`
- **Volumes**: `./task1:/app/task1`
- **Depends on**: `db`
- **Command**: Runs `python task1/app.py`

### 3. Task2 (`task2`)
- **Container name**: `crm_task2`
- **Build**: `Dockerfile.task2`
- **Volumes**: `./task2:/app/task2`
- **Ports**: `8050:8050`


The project consists of three main services defined in the `docker-compose.yml` file:

* `db`: A **PostgreSQL 15** database service.
* `task1`: A Python service that runs the `task1/app.py` that generate Complaint Resolution Analysis (static PDF report).
* `task2`: A Python service that create interactive Plotly Dash app based on `LuxuryLoanPortfolio.csv`.


### 🚀 Getting Started
1.  Unzip the zip files
2.  Build and run the containers
    ```sh
    docker-compose up -d --build
    ```
### Start task 1 and task 2
```sh
docker-compose build task1
docker-compose up task1
```

```sh
docker-compose build task2
docker-compose up task2
```


