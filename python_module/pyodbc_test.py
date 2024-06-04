import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv("SERVER")
UID = os.getenv("DB_USER")
PWD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DATABASE")

connect_info = 'Driver={}; Server={}; uid={}; pwd={}; Database={};'.format("SQL Server", SERVER, UID, PWD, DATABASE)

conn = pyodbc.connect(connect_info)

cursor = conn.cursor()

cursor.execute("CREATE TABLE grades (grade_id int not null identity(1, 1) primary key, course varchar(255) not null, )")
# cursor.execute("INSERT INTO users (name, age) values ('文台湖', 23)")
# cursor.execute("UPDATE users SET age = 33  WHERE name='文台湖'")

# conn.commit()

df = pd.read_sql("SELECT * FROM users", conn)

cursor.execute("SELECT * FROM users")

for row in cursor:
    print(row)

print(df)

conn.close()