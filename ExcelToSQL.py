import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load env variables from .env file
load_dotenv()

# Database variables
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os. getenv('DB_PORT')

# Excel File Path
excel_file_path = os.getenv('EXCEL_FILE_PATH')
sheet_name = os.getenv('EXCEL_SHEET')

# PostgreSQL table name
table_name = os.getenv('TABLE_NAME')

# Define Postgre connection URL
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create engine to connect to database
engine = create_engine(db_url)

# Read Excel sheet into df
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Insert data into PostgreSQL db
df.to_sql(table_name, engine, if_exists='replace', index=False)

print("Data inserted successfully!")