import pandas as pd
import numpy as np

# Lấy ra value của một cặp key-value trong trường parameter
def get_param_value(row,column,param_key='' ):
    event_field = row[column]
    if column == "event_params_key":
        return event_field.get(param_key)
    else:
        return event_field

def get_dataframe_session(df):
    # Extract dữ liệu từ các field dạng dict
    df_session = df[['user_pseudo_id', 'event_timestamp', 'event_params_key']]
    df_session.loc[:, 'session_id'] = df_session['event_params_key'].apply(lambda x: x.get('ga_session_id', None))
    df_session.loc[:, 'duration'] = df_session['event_params_key'].apply(lambda x: x.get('engagement_time_msec', np.nan))
    
    # Sắp xếp lại các cột
    reordered_fields = ['session_id', 'user_pseudo_id', 'event_timestamp', 'duration']
    df_session_final = df_session[reordered_fields]
    
    # Đổi lại tên các cột
    selected_fields = ['session_id', 'user_id', 'start_time', 'duration']
    df_session_final.columns = selected_fields

    return df_session_final