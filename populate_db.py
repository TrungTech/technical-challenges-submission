import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Define database connection details and file path
DB_USER = os.getenv("POSTGRES_DB_USER")
DB_PASSWORD = os.getenv("POSTGRES_DB_PASSWORD") 
DB_HOST = os.getenv("POSTGRES_DB_HOST")  
DB_PORT = os.getenv("POSTGRES_DB_PORT")
DB_NAME = "default"
TABLE_NAME = "user_behaviour"

DATA_FILE_PATH = "cleaned_data/cleaned_data.csv"

def populate_database():
    """Reads data from a CSV file and populates a PostgreSQL database."""

    try:
        print(f"Reading data from {DATA_FILE_PATH}...")
        df = pd.read_csv(DATA_FILE_PATH)
        print(f"Successfully read {len(df)} records from {DATA_FILE_PATH}.")

        engine_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        print(f"Connecting to database: {DB_HOST}:{DB_PORT}/{DB_NAME}")
        engine = create_engine(engine_string)

        print(f"Writing data to table '{TABLE_NAME}'...")
        df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False, chunksize=1000)
        print(f"Successfully populated '{TABLE_NAME}' table with {len(df)} records.")

    except FileNotFoundError:
        print(f"Error: Data file not found at {DATA_FILE_PATH}")
    except pd.errors.EmptyDataError:
        print(f"Error: Data file is empty at {DATA_FILE_PATH}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    populate_database() 