import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://username:passwd@host/database')

update_table = pd.read_sql_table('table_name', engine)
