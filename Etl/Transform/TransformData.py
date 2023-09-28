import pandas as pd
import json

class TransformData:
    
    # def transform data
    @staticmethod
    def transform_data(dataframe, transformations):
        for column, transformation in transformations.items():
            dataframe[column] = transformation(dataframe[column])
        return dataframe
    
    @staticmethod
    def convert_objectid_to_string(df):
    # Tìm tất cả các cột có kiểu dữ liệu là 'object' (bao gồm ObjectID)
        object_cols = df.select_dtypes(include=['object']).columns
    
        for col in object_cols:
            try:
                # Thử chuyển đổi từng giá trị trong cột thành chuỗi
                df[col] = df[col].astype(str)
            except:
                print(f"Không thể chuyển đổi cột {col} thành chuỗi.")
    
        return df


    # def transform dict to string
    @staticmethod
    def transform_dict_to_string(value):
        if isinstance(value, object):
            return str(value)
        return value

    # def transform timestamp
    @staticmethod
    def transform_timestamp(timestamp_column):
        timestamp_column = pd.to_datetime(timestamp_column, errors= 'coerce', format='%Y-%m-%d %H:%M:%S')
        return timestamp_column
    
    # def transform date
    @staticmethod
    def transform_date(column):
        column = pd.to_datetime(column, format='%Y%m%d')
        return column
