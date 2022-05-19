-- Project: SuperSports
-- SUPERSPORTS database
-- Group 125
-- Members: Noble Koshy, Brahm Rifino

SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;

DROP TABLE IF EXISTS  departments, employees, items, returns, return_details, sales, sale_details;
-- -----------------------------------------------------
-- Table structure for table departments
-- -----------------------------------------------------

CREATE TABLE departments (
  department_id int NOT NULL AUTO_INCREMENT,
  department_name varchar(45) NOT NULL,
  location varchar(45) NOT NULL,
  PRIMARY KEY (department_id)
);

-- -----------------------------------------------------
-- Table structure for table employees
-- -----------------------------------------------------

CREATE TABLE employees (
  employee_id int NOT NULL AUTO_INCREMENT,
  first_name varchar(45) DEFAULT NULL,
  last_name varchar(45) DEFAULT NULL,
  PRIMARY KEY (employee_id)
);

-- -----------------------------------------------------
-- Table structure for table items
-- -----------------------------------------------------

CREATE TABLE items (
	item_id int NOT NULL AUTO_INCREMENT,
	name varchar(45) NOT NULL,
	brand varchar(45) NOT NULL,
	price decimal(7,2) NOT NULL,
	clearance tinyint(4) NOT NULL,
	departments_department_id int,
	PRIMARY KEY (item_id),
	FOREIGN KEY (departments_department_id) REFERENCES departments(department_id) ON DELETE SET NULL
	ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table structure for table returns
-- -----------------------------------------------------

CREATE TABLE returns (
  return_id int NOT NULL AUTO_INCREMENT,
  return_date datetime NOT NULL,
  employees_employee_id int,
  PRIMARY KEY (return_id),
  FOREIGN KEY (employees_employee_id) REFERENCES employees(employee_id) ON DELETE SET NULL
  ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table structure for table return_details
-- -----------------------------------------------------

CREATE TABLE return_details (
  return_details_id int NOT NULL AUTO_INCREMENT,
  returns_return_id int,
  items_item_id int,
  PRIMARY KEY (return_details_id),
  FOREIGN KEY (returns_return_id) REFERENCES returns(return_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (items_item_id) REFERENCES items(item_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table structure for table sales
-- -----------------------------------------------------

CREATE TABLE sales (
	sale_id int NOT NULL AUTO_INCREMENT,
	sale_date datetime NOT NULL,
	employees_employee_id int,
	PRIMARY KEY (sale_id),
	FOREIGN KEY (employees_employee_id) REFERENCES employees(employee_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table structure for table sale_details
-- -----------------------------------------------------

CREATE TABLE sale_details (
	sale_details_id int NOT NULL AUTO_INCREMENT,
	items_item_id int,
	sales_sale_id int,
	PRIMARY KEY (sale_details_id),
	FOREIGN KEY (items_item_id) REFERENCES items(item_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (sales_sale_id ) REFERENCES sales(sale_id ) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- data INSERT statements
-- -----------------------------------------------------

INSERT INTO departments (department_name, location) VALUES
	('sports', 'first floor'),
	('exercise', 'second floor'),
	('outdoors', 'third floor');


INSERT INTO employees (first_name, last_name) VALUES
	('john', 'doe'),
	('peter', 'parker'),
	('jane', 'doe');


INSERT INTO items (name, brand, price, clearance, departments_department_id) VALUES
	('basketball', 'wilson', '50.00', 0, 1),
	('baseball glove', 'nike', '100.00', 0, 1),
	('treadmill', 'peloton', '300.00', 1, 2);

INSERT INTO returns (return_date, employees_employee_id) VALUES
	('2022-04-07 05:02:56', 1),
	('2022-04-20 05:02:56', 2),
	('2022-04-29 05:02:56', 3);


INSERT INTO return_details (returns_return_id, items_item_id) VALUES
	(1, 1),
	(2, 2),
	(3, 3);

INSERT INTO sales (sale_date, employees_employee_id) VALUES
	('2022-04-01 05:05:40', 1),
	('2022-04-02 05:05:40', 2),
	('2022-04-29 05:05:40', 3);


INSERT INTO sale_details (items_item_id, sales_sale_id) VALUES
	(1, 1),
	(2, 2),
	(3, 3),
	(2, 3),
	(1, 3);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;