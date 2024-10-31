CREATE TABLE books_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(255),
    author VARCHAR(255),
    year_published INT,
    ISBN VARCHAR(20)
);


CREATE TABLE borrower_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    borrower_name VARCHAR(255),
    borrowed_date DATE,
    return_date DATE,
    overdue_flag BOOLEAN,
    FOREIGN KEY (book_id) REFERENCES table1(id)
);