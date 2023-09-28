# database/__init__.py
import os
import yaml

# Xác định đường dẫn tới thư mục chứa file ETL/Load/__init__.py
load_dir = os.path.dirname(os.path.abspath(__file__))

# Xác định đường dẫn tới thư mục ETL/ từ thư mục ETL/Load/
etl_dir = os.path.abspath(os.path.join(load_dir, '..'))

# Xác định đường dẫn tới thư mục config từ thư mục gốc my_project/
config_dir = os.path.abspath(os.path.join(etl_dir, '..', 'config'))

# Xác định đường dẫn tới file config.yaml
config_file_path = os.path.join(config_dir, 'config.yaml')

# Đọc file cấu hình YAML
with open(config_file_path, 'r') as file:
    config_data = yaml.safe_load(file)

# Export thông tin cấu hình ra để sử dụng trong file kết nối database
database_config = config_data['database']
host = database_config['host']
port = database_config['port']
user = database_config['user']
password = database_config['password']
dbname = database_config['dbname']
