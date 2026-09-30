# Database Notes

## Foreign Key, Primay Key & Not Null Constraint

```SQL
CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name TEXT
);
```

```SQL
CREATE TABLE employees (
  id INT PRIMARY KEY NOT NULL,
  name TEXT,
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

---

## Insert & Select Commands

```SQL
INSERT INTO departments (dept_id, dept_name)
VALUES (1, 'IT'), (2, 'DEVOPS'), (3, 'TESTING'), (4, 'AI');

SELECT * FROM departments;
```

```SQL
INSERT INTO employees (id, name, dept_id)
VALUES (1, 'Aman', 1), (2, 'Manoj', 2);

SELECT * FROM employees;
```

---

## CRUD Operations

### SELECT (Read)

- Retrieve data from the table
- Not modify data

```SQL
SELECT * FROM <table_name>;
```

#### Column Aliasing

```SQL
SELECT column_name_1 AS cn1, column_name_2 AS cn2 FROM <table_name>;
```

#### Using Arithmetic in SELECT

```SQL
CREATE TABLE employees (
  id INT PRIMARY KEY NOT NULL,
  name TEXT,
  department TEXT,
  salary INT
);

INSERT INTO employees (id, name, department, salary) VALUES
(1, 'Rahul', 'IT', 70000),
(2, 'Neha', 'HR', 60000),
(3,'Aman', 'IT', 80000),
(4, 'Sara', 'Finance', 75000);

SELECT * FROM employees;

SELECT name, (salary * 12) AS yearly_salary FROM employees;
```

### WHERE Clause

WHERE filters rows based on conditions.

- pandas equivalent: if df['col'] == value:
- SQL equivalent:

  - PS: Employees where department = IT
  - ```SQL
    SELECT * FROM employees WHERE department = 'IT';
    ```

### Comparison Operators

Comparison operators are used inside WHERE clause.

| Symbol | Meaning                  |
| ------ | ------------------------ |
| >      | Greater than             |
| <      | Less than                |
| =      | Equal to                 |
| >=     | Greater than or equal to |
| <=     | Less than or equal to    |
| !=     | Not equal to             |

- P.S. : Salary greater than 70000
- ```SQL
  SELECT * FROM employees WHERE salary > 70000;
  ```

### AND, OR operators

- P.S. : Employees from IT department and salary above 75000
- ```SQL
  SELECT * FROM employees WHERE department = 'IT' AND salary > 75000;
  ```
- P.S. : Employees from IT department or salary above 75000
- ```SQL
  SELECT * FROM employees WHERE department = 'IT' OR salary > 75000;
  ```

### BETWEEN

Used to filter values within a range and it is inclusive in nature.

- P.S. : Employees with salary between 65000 and 80000
- ```SQL
  -- without BETWEEN
  SELECT * FROM employees WHERE salary >= 65000 AND salary <= 80000;

  -- with BETWEEN
  SELECT * FROM employees WHERE salary BETWEEN 65000 AND 80000;
  ```

### IN Operator

Used when matching multiple values.

- P.S. : Employees from Delhi or Bengaluru
- ```SQL
  SELECT * FROM employees WHERE city IN ('Delhi', 'Bengaluru');
  ```
- P.S. : Employees named Rahul or Aman
- ```SQL
  -- without IN
  SELECT * FROM employees WHERE name IN ('Rahul', 'Aman');

  -- with IN
  SELECT * FROM employees WHERE name IN ('Rahul', 'Aman');
  ```

### LIKE (Pattern Matching)

Used for searching text patterns.

% (Wildcards) - any character

_ (Wildcards) - single character

- P.S. : Names starting with R
- ```SQL
  SELECT * FROM employees WHERE name LIKE 'R%';
  ```
- P.S. : Names ending with R
- ```SQL
  SELECT * FROM employees WHERE name LIKE '%R';
  ```
- P.S. : Names ending with a
- ```SQL
  SELECT * FROM employees WHERE name LIKE '%a';
  ```
- P.S. : Names having exactly 4 letters
- ```SQL
  SELECT * FROM employees WHERE name LIKE '____';
  ```

### ORDER BY

Used to sort results.

- P.S. : Sort by salary
- ```SQL
  -- ascending order
  SELECT * FROM employees ORDER BY salary;

  -- descending order
  SELECT * FROM employees ORDER BY salary DESC;

  -- multiple sorting
  SELECT * FROM employees ORDER BY department, salary DESC;
  ```

### LIMIT (Top N results)

Used to restrict number of rows returned.

```SQL
SELECT * 
FROM employees 
ORDER BY salary DESC 
LIMIT 3;
```

P.S. : Top-1 (from bottom) Lowest salary

```SQL
SELECT * FROM employees ORDER BY salary LIMIT 1;
```
