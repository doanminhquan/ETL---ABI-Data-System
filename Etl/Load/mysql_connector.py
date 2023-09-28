# import mysql.connector
# from Etl.Transform import TransformData
# import pandas as pd
# import mysql.connector
# from . import host, port, user, password, dbname

# # Thực hiện kết nối tới MySQL
# def connect_mysql():
#     mydb = mysql.connector.connect(
#         host = host,
#         port = port,
#         user = user,
#         password = password
#     )
#     return mydb

# # Tạo database
# def create_db(mydb: mysql.connector.connection.MySQLConnection):
#     mycursor = mydb.cursor(dictionary=True)
#     # Thực hiện lệnh sql trong file
#     with open('D:\Python\DemoETLMongoDBtoSQL\Etl\Load\CreateDatabase.sql', 'r') as sql_file:
#         for sql_statement in sql_file.read().split(';'):
#             if sql_statement.strip():
#                 mycursor.execute(sql_statement)
#                 mydb.commit()  # Commit each statement individually

# # Thực hiện ghi dữ liệu vào MySQL
# def insert_data(mydb: mysql.connector.connection.MySQLConnection, df: pd.DataFrame, sql_insert):
#     mycursor = mydb.cursor(dictionary=True)
#     # Insert data vào MySQL
#     for i, row in df.iterrows():
#         transformed_row =row.apply(TransformData.TransformData.transform_dict_to_string)
#         values = tuple(transformed_row.values)
#         try:
#             mycursor.execute(sql_insert, values)
#             mydb.commit()
#         except mysql.connector.Error as err:
#             print("Error: ", err)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from Etl.Transform import TransformData
import pandas as pd
from . import host, port, user, password, dbname

# Tạo engine kết nối tới MySQL bằng SQLAlchemy
def create_engine_mysql():
    db_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(db_url)
    return engine

# Tạo session để thao tác với cơ sở dữ liệu
def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# Tạo database (Không cần chạy các lệnh SQL từ file, SQLAlchemy sẽ tự động tạo cơ sở dữ liệu nếu chưa có)
def create_db(engine):
    pass

# Thực hiện ghi dữ liệu vào MySQL
def insert_data(engine, df, table_name):
    converted_df = TransformData.TransformData.convert_objectid_to_string(df)    
    try:
        converted_df.to_sql(table_name, con=engine, if_exists='append', index=False)
    except SQLAlchemyError as err:
        print("Error: ", err)
