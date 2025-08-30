import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]"
)

update_table = pd.read_sql_table("table_name", engine)
