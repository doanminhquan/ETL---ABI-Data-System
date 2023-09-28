import Etl.Extract.mongodb_connector as mongo
import Etl.Transform.TransformData as TransformData
import Etl.Transform.TransformDataIntoTableSession as tftbl
import Etl.Load.mysql_connector as sql
import pandas as pd

# Kết nối tới MongoDB
mongodb_connection = mongo.connect_mongodb()

# Lấy dữ liệu từ MongoDB và chuyển thành dataframe
data_event = mongo.get_data_collection_into_df(mongodb_connection, 'event')
data_session = tftbl.get_dataframe_session(data_event)

# Dictionary chứa các hàm biến đổi cần thực hiện
transformations_event = {
    'event_date': TransformData.TransformData.transform_date,
    'event_timestamp': TransformData.TransformData.transform_timestamp,
    'event_previous_timestamp': TransformData.TransformData.transform_timestamp
}

# Chạy các hàm transform
transformed_data_event = TransformData.TransformData.transform_data(data_event, transformations_event)
transformed_data_session = tftbl.get_dataframe_session(transformed_data_event)
print((transformed_data_session))
# Kết nối tới MySQL
engine = sql.create_engine_mysql()
session = sql.create_session(engine)

# Ghi dữ liệu vào MySQL
sql.insert_data(engine=engine, df=transformed_data_event, table_name='event')
sql.insert_data(engine=engine, df=transformed_data_session, table_name='session')