# Extract/__init__.py
import os
import yaml

# Xác định đường dẫn tới thư mục chứa file ETL/Extract/__init__.py
load_dir = os.path.dirname(os.path.abspath(__file__))

# Xác định đường dẫn tới thư mục ETL/ từ thư mục ETL/Extract/
etl_dir = os.path.abspath(os.path.join(load_dir, '..'))

# Xác định đường dẫn tới thư mục config từ thư mục gốc
config_dir = os.path.abspath(os.path.join(etl_dir, '..', 'config'))

# Xác định đường dẫn tới file config.yaml
config_file_path = os.path.join(config_dir, 'config.yaml')

# Đọc file cấu hình YAML
with open(config_file_path, 'r') as file:
    config_data = yaml.safe_load(file)

# Trích xuất các biến cấu hình từ config_data
mongodb_config = config_data['mongodb']
host = mongodb_config['host']
port = mongodb_config['port']
dbname = mongodb_config['dbname']


