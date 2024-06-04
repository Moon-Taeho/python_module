import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv("SERVER")
UID = os.getenv("DB_USER")
PWD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DATABASE")

# connect_info = 'Driver={SQL SERVER}; Server=' + os.environ["SERVER_NAME"] + '; uid=' + os.environ["USER_ID"] + '; pwd=' + os.environ["USER_PWD"] + '; Database=' + os.environ["DATABASE_NAME"] + ';'

connect_info = 'Driver={}; Server={}; uid={}; pwd={}; Database={};'.format("SQL Server", SERVER, UID, PWD, DATABASE)
""" conn = pyodbc.connect('Driver={SQL Server};' #ドライバ
                                'Server={os.environ["SERVER_NAME]"};' # サーバー名
                                'uid={os.environ["USER_ID"]};' # ユーザーID
                                'pwd={os.environ["USER_PWD"]};' # ユーザーパスワード
                                'Database={os.environ["DATABASE_NAME"]};' # データベース名
                                ) """

conn = pyodbc.connect(connect_info)

cursor = conn.cursor() # 接続したデータベースの情報をカーソルに移動

# pandasとpyodbcを連携して活用できる
# df = pd.read_sql("SELECT * FROM 拠点", conn)

# cursorを使えば変更を見れるのに、実際のデータベースには変更されない
cursor.execute('INSERT INTO USERS (name, age) VALUES (문태호, 23)')

# commitすれば実際のデータベースにも適用
# conn.commit()

for row in cursor:
    print(row)

# 接続終了
conn.close()