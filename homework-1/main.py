"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
from config import *


def read_customers_data():
    # Функция создает список кортежей из данных файла customers_data.csv
    with open(CUST_DATA, newline='') as file:
        reader = csv.DictReader(file)
        customers_list = []
        for row in reader:
            rez = (row['customer_id'], row['company_name'], row['contact_name'])
            customers_list.append(rez)
    return customers_list


def read_employees_data():
    # Функция создает список кортежей из данных файла employees_data.csv
    with open(EMP_DATA, newline='') as file:
        reader = csv.DictReader(file)
        employees_list = []
        for row in reader:
            rez = (
                row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes'])
            employees_list.append(rez)
    return employees_list


def read_orders_data():
    # Функция создает список кортежей из данных файла orders_data.csv
    with open(ORD_DATA, newline='') as file:
        reader = csv.DictReader(file)
        orders_list = []
        for row in reader:
            rez = (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city'])
            orders_list.append(rez)
    return orders_list


customers_data = read_customers_data()
employees_data = read_employees_data()
orders_data = read_orders_data()

# Считываем пароль для BD
with open(PASSWORD) as file:
    password = file.read()


def connect_bd():
    # подключени к BD
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password=password
    )

    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany("insert into employees values(%s, %s, %s, %s, %s, %s)", employees_data)
                cur.executemany("insert into customers values(%s, %s, %s)", customers_data)
                cur.executemany("insert into orders values(%s, %s, %s, %s, %s)", orders_data)
    finally:
        conn.close()


if __name__ == '__main__':
    connect_bd()
