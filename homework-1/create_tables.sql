-- SQL-команды для создания таблиц
create table employees
(
	employee_id int primary key,
	first_name varchar(30) not null,
	last_name varchar(30) not null,
	title varchar(30) not null,
	birth_date date not null,
	notes text
);

create table customers
(
	customer_id varchar(30) primary key,
	company_name varchar(100) not null,
	contact_name varchar(30) not null
);

create table orders
(
	order_id int primary key,
	customer_id varchar(30) references customers(customer_id),
	employee_id int references employees(employee_id),
	order_date date not null,
	ship_city varchar(30) not null
)