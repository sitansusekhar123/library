# How to run?

## Download MySQL

1. Go to [Installer Website](https://dev.mysql.com/downloads/installer/)

2. Select Windows, latest version 8.0.40.

3. Download the Windows (x86, 32-bit), MSI Installer. Size is around 300 MB.

4. In the login page, click on "No thanks, just start my download."

## Installation

Installer must be downloaded to the Downloads folder.

1. Open the installer.

2. Select "Server only" and click "Next".

3. Click Execute. Let it run and then click Next.

4. In Type and Networking, keep everything as default and click Next.

5. In the Authentication Method, select "Use Strong Password Encryption" and click Next.

6. In Accounts and Roles, enter a Root Password. For this example keep the password `mysql`. (Remember it) and click Next.

7. In Accounts and Roles, click Add User. Enter a username and password. Keep the username as `mysql_user` and password as `mysql`. Click OK and then Next. Remember the username and password.

8. In Windows Service, keep everything as default and click Next.

9. In Server File Permission, keep everything as default and click Next.

10. In Apply Configuration, click Execute. Let it run and then click Finish.

11. In Product Configuration, click Next and then Finish.

IMPORTANT: TO BE EVERYTHING EASY, KEEP THE USER PASSWORD AND ROOT PASSWORD THE SAME FOR NOW.

## Setting up MySQL

1. Go to start and search for MySQL 8.0 Command Line Client.

2. Enter the password for the root user.

3. Enter the following commands. Note copy and paste the commands one by one until each semicolon.

```sql
CREATE DATABASE library;

USE library;

CREATE TABLE books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year_published INT NOT NULL,
    ISBN VARCHAR(20) UNIQUE NOT NULL,
    copies INT NOT NULL DEFAULT 1
);

CREATE TABLE loans (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    borrower_name VARCHAR(255) NOT NULL,
    borrowed_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

CREATE TABLE reservations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    reserver_name VARCHAR(255) NOT NULL,
    reservation_date DATE NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);
```

4. To check if the tables were created, enter the following commands.

```sql
SHOW TABLES;
```

Output should be:
    
```
+----------------+
| Tables_in_library |
+----------------+
| books          |
| loans          |
| reservations   |
+----------------+
3 rows in set (0.00 sec)
```

5. Lets populate the books table with some data. For this copy paste everything at once in the file `books_data_populate.sql` in the repository.

6. Once done, it should show the following output.

```
Query OK, 91 rows affected (0.04 sec)
Records: 91  Duplicates: 0  Warnings: 0
```

7. To check if the data was populated, enter the following command.

```sql
SELECT * FROM books;
```

Output should be:

```
+----+---------------------------------+---------------------+----------------+------------------+--------+
| id | book_name                       | author              | year_published | ISBN             | copies |
+----+---------------------------------+---------------------+----------------+------------------+--------+
|  1 | The Great Gatsby                | F. Scott Fitzgerald |          1925  | 9780743273565    |      1 |
|  2 | To Kill a Mockingbird           | Harper Lee          |          1960  | 9780061120084    |      1 |
```


## Setting up Python

1. Make sure Python is installed. If not, go to [Python Website](https://www.python.org/downloads/) and download the latest version.

2. Open the command prompt and enter the following commands.

```bash
pip install mysql-connector-python
```

## Download the Repository

1. Go to the repository and click on the green button "Code" at the top right.

2. Click on "Download ZIP".

3. Copy the ZIP file to a new folder say under `Documents/Assignment`.

4. Extract the ZIP file.

## Run Code
1. Open the command prompt `CMD`.

2. See the path: `C:\Users\Username>`. Username is the name of the user.

3. If in the above path, then navigate to the code folder by typing the following:
    
```bash
cd Documents
cd Assignment
```

Otherwise, type the following:
    
```bash
cd C:\Users\<Username>\Documents\Assignment
```

Here, the `<Username>` is the name of the user. It can be `Saksham`.

4. To run the code, type the following:

```bash
python main.py
```

5. The code will run and show the following output.

```bash
Welcome to the Library Management CLI. Type 'help' to see the commands.
```

6. Enter command: `help`
Output: 

```bash
The following commands are available:
Available commands:
- add_book "book_name" "author" year_published "ISBN" [copies]
- remove_book "book_name" "author"
- look_up_books [--book_name="book_name"] [--author="author"] [--year_published=year]
- search_books "keyword"
- is_book_lent "book_name"
- get_return_date "book_name"
- get_books_ordered order_by
- group_books_by_year
- get_borrower_details
- lend_book "book_name" "borrower_name" "borrowed_date" "due_date"
- return_book "book_name" "return_date"
- view_overdue_books "current_date"
- calculate_fines "current_date" fine_per_day
- extend_due_date "book_name" "new_due_date"
- reserve_book "book_name" "reserver_name" "reservation_date"
- cancel_reservation "book_name" "reserver_name"
- view_reservations
- view_book_availability
- generate_report
- export_books "filename.csv"
```
