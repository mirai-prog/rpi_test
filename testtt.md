'''
SELECT * FROM dept, emp;
SELECT * FROM ord, item, product;
SELECT e.first_name, e.last_name, d.name AS Dzial FROM emp e JOIN dept d ON e.dept_id = d.id WHERE d.name = 'Sales';
SELECT first_name, last_name, name FROM emp, dept WHERE dept.id = emp.dept_id AND name = 'Sales';
SELECT e.first_name, e.last_name, d.name AS Dzial, r.name AS Region FROM emp e JOIN dept d ON e.dept_id = d.id JOIN region r ON d.region_id = r.id WHERE r.name = 'Europe';
SELECT w.address AS `Adres hurt.`, CONCAT(m.first_name, ' ', m.last_name) AS `Szef`, p.name AS `Nazwa produktu`, i.amount_in_stock AS `Stan biez.`, i.max_in_stock AS `Stan max`, (i.max_in_stock - i.amount_in_stock) AS `Roznica` FROM inventory i JOIN warehouse w ON i.warehouse_id = w.id JOIN emp m ON w.manager_id = m.id JOIN product p ON i.product_id = p.id WHERE (i.max_in_stock - i.amount_in_stock) < 10 ORDER BY w.address, p.name;
CREATE TABLE price_category (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(30), price_min DECIMAL(10,2), price_max DECIMAL(10,2)); INSERT INTO price_category (name, price_min, price_max) VALUES ('Low Summer',0,100),('Medium Summer',101,500),('High Summer',501,2000),('Low Winter',0,50),('Medium Winter',51,300),('High Winter',301,2000); SELECT p.name AS `Nazwa produktu`, c.name AS `Nazwa przedzialu`, CONCAT(c.price_min,' -- ',c.price_max) AS `Przedzial`, p.suggested_price AS `Cena` FROM product p JOIN price_category c ON p.suggested_price BETWEEN c.price_min AND c.price_max;
SELECT e.last_name AS `Pracownik`, e.title AS `Stanowisko`, m.last_name AS `Szef`, m.title AS `Stanowisko szefa` FROM emp e LEFT JOIN emp m ON e.manager_id = m.id ORDER BY e.manager_id;
UPDATE ord SET sales_rep_id = NULL WHERE id < 100; SELECT o.id, DATE_FORMAT(o.date_ordered, '%d-%m-%Y') AS `Data`, IFNULL(e.first_name, '--brak danych--') AS `Imie`, IFNULL(e.last_name, '--brak danych--') AS `Nazwisko` FROM ord o LEFT JOIN emp e ON o.sales_rep_id = e.id;
SELECT e.first_name, e.last_name, o.id, DATE_FORMAT(o.date_ordered, '%d-%m-%Y') AS date_ordered FROM emp e LEFT JOIN ord o ON e.id = o.sales_rep_id ORDER BY e.last_name;
SELECT name FROM region UNION SELECT name FROM dept; SELECT name FROM region UNION ALL SELECT name FROM dept;
SELECT CONCAT(last_name, '  <-- emp') AS `Pracownicy i klienci` FROM emp UNION SELECT CONCAT(name, '  <-- customer') FROM customer ORDER BY 1;
SELECT 1 AS typ, CONCAT(last_name, '  <-- emp') AS `Pracownicy i klienci` FROM emp UNION ALL SELECT 2 AS typ, CONCAT(name, '  <-- customer') FROM customer ORDER BY typ, `Pracownicy i klienci`;
'''