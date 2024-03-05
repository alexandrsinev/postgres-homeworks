from pathlib import Path

ROOT_DIR = Path(__file__).parent
CUST_DATA = Path(ROOT_DIR, 'homework-1', 'north_data', 'customers_data.csv')
EMP_DATA = Path(ROOT_DIR, 'homework-1', 'north_data', 'employees_data.csv')
ORD_DATA = Path(ROOT_DIR, 'homework-1', 'north_data', 'orders_data.csv')
PASSWORD = Path(ROOT_DIR, 'password.txt')