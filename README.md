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

6. In Accounts and Roles, enter a Root Password. (Remember it) and click Next.

7. In Accounts and Roles, click Add User. Enter a username and password. Click OK and then Next. Remember the username and password.

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


## Run PIP

## Run Code
