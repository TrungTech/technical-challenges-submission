# Data Engineer Test Submission

**Stage 1**: *CLEAN* - Data cleaning using pandas performed via `/explore_and_clean_data.ipynb`, output stored in `/cleaned_data/cleaned_data.csv`

**Stage 2**: *INGEST* - Load cleaned data into PostgreSQL database using `/populate_db.py`

**Stage 3**: *ANALYSE* - `/analyse.sql` provide answers of questions

**Stage 4**: *PRODUCTIONISATION* - Below is my stategy

Solution 1: Python with Cron/Task Scheduler
- Description:
    - Create a Python script that connects to PostgreSQL database
    - For each query, the script executes it and processes the results (e.g., write to csv file, insert to report)
    - Use a system scheduler like cron (on Linux/macOS) or Task Scheduler (on Windows) to run this Python script at a specific time each day.
- Pros:
    - Relatively easy to set up. Have full control over the environment.
    - Allows for custom logic before or after query execution (e.g., sending email notifications with results, custom formatting).
- Cons:
    - Depends on the machine where the cron job runs. If the machine is down, the job fails. 
    - Requires custom implementation for robust monitoring (did the job run? did it succeed/fail?) and alerting.

Solution 2: Database-Native Scheduling (pgAgent or pg_cron extension)
- Description:
    - Schedule SQL queries directly in postgres
- Pros:
    - Runs directly within the database, minimizing external dependencies for the query execution itself.
    - Tightly coupled with database transactions.
- Cons:
    - Limited to only working with PostgreSQL database system.
    - Harder to perform actions outside the database (e.g., sending email notifications with results, custom formatting).
    - Capabilities vary and are often less user-friendly than dedicated orchestration tools.


Solution 3: Orchestration by Apache Airflow
- Description:
    - Create a DAG with PostgresOperator tasks to execute SQL queries
    - Or use SSHOperator to execute the Python script (same as Solution 1 but use Airflow for scheduling and triggering)
- Pros:
    - Excellent for complex dependencies, automated retries, backfills, and visualizing data pipelines.
    - Easy tracking job status and logs.
    - Can be scaled and integrated with many systems.
- Cons:
    - More complex to set up 
    - For a few simple daily queries, this might be an over-engineered solution.
