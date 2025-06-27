# Discovering Databases: An Easy Start for Beginners

## Overview
This is a beginner-friendly project designed to introduce the foundational concepts of databases and SQL (Structured Query Language). This project covers the essentials of database creation, table management, and data manipulation using MySQL, as well as integrating Python with MySQL for programmatic database operations. The project is structured around creating a database schema for an online bookstore (alx_book_store) and performing various tasks to interact with it.

## Learning Objectives

By completing this project, you will:
- Understand what a database and relational database are.
- Learn what SQL stands for and how to use MySQL.
- Master creating and altering tables using Data Definition Language (DDL).
- Perform CRUD operations (Create, Read, Update, Delete) using Data Manipulation Language (DML).
- Execute SQL queries to list and describe tables.
- Integrate Python with MySQL using the mysql-connector-python library.

  
## Repository Structure
```Intro_to_DB/
├── alx_book_store.sql  # Task 0: Full database schema
├── MySQLServer.py      # Task 1: Python script to create database
├── task_2.sql          # Task 2: Create tables
├── task_3.sql          # Task 3: List tables
├── task_4.sql          # Task 4: Describe Books table
├── task_5.sql          # Task 5: Insert single customer
├── task_6.sql          # Task 6: Insert multiple customers
└── README.md           # This file
```

## How to Test
**1. Set Up MySQL:**
- Ensure MySQL is running.
- Log in to MySQL: `mysql -u myusername -p`
- Create the database manually if testing without `MySQLServer.py`: `CREATE DATABASE alx_book_store;`


**2. Run Python Script:**
```bash
python3 MySQLServer.py
```

- Expected output: `Database 'alx_book_store' created successfully!` or an error message if connection fails.

**3. Run SQL Scripts:**
```bash
mysql -u yourusername -p alx_book_store < alx_book_store.sql
mysql -u yourusername -p alx_book_store < task_2.sql
mysql -u yourusername -p alx_book_store < task_3.sql
mysql -u yourusername -p alx_book_store < task_4.sql
mysql -u yourusername -p alx_book_store < task_5.sql
mysql -u yourusername -p alx_book_store < task_6.sql
```

**4. Verify Results:**
- After `task_3.sql`, check output for table names.
- After `task_4.sql`, check column metadata for the `Books` table.
- After `task_5.sql` and `task_6.sql`, query `Customers` to confirm inserted data:

```sql
SELECT * FROM Customers;
```

## Notes
- **SQL Keywords**: All SQL scripts use uppercase keywords (e.g., `CREATE`, `INSERT`).
- **Error Handling**: The Python script (`MySQLServer.py`) includes try-except blocks to handle connection errors.
- **Constraints:**
    - Task 1 (`MySQLServer.py`) must not use `SELECT` or `SHOW` statements.
    - Task 4 (`task_4.sql`) must not use `DESCRIBE` or `EXPLAIN` statements.
- **Foreign Keys**: Ensure tables are created in order (`Authors`, `Customers`, `Books`, `Orders`, `Order_Details`) to satisfy foreign key dependencies.
