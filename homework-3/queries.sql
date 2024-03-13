-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
SELECT cu.company_name, CONCAT(first_name, ' ', last_name) as employee
FROM orders as o
JOIN customers as cu USING(customer_id)
JOIN employees as e USING(employee_id)
JOIN shippers as s ON o.ship_via = s.shipper_id
where cu.city = 'London' and e.city = 'London' and s.shipper_id = 2

-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.
select product_name, units_in_stock, contact_name, phone from products
join suppliers on products.supplier_id = suppliers.supplier_id
join categories on products.category_id = categories.category_id
where discontinued = 0 and units_in_stock < 25 and categories.category_name in ('Dairy Products', 'Condiments')
order by units_in_stock

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
select company_name from customers
except
select distinct company_name from orders
join customers using(customer_id)
where orders.customer_id = customers.customer_id


-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.
select distinct product_name from products
where product_id in (select product_id from order_details where quantity = 10)
