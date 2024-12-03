# Outputs

## Running Code - First Step

1. The code is run by typing ```python main.py``` on the command line.

2. Running the code shows the output as below:

```
Welcome to the Library Management CLI. Type 'help' to see available commands.
Enter command:
```

3. Entering ```help``` command list all the different library help functions which are available such as:

```
Welcome to the Library Management CLI. Type 'help' to see available commands.
Enter command: help

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

Below, each and every command is explained in detail along with the expected output and what effect it has on the MySQL Database.

### Add Book

The `add_book` command is used to add a new book to the library database. The command takes in the following parameters:

- `book_name`: The name of the book to be added.
- `author`: The author of the book.
- `year_published`: The year the book was published.
- `ISBN`: The ISBN of the book.
- `copies`: The number of copies of the book to be added.

The command is used as follows:

```
add_book "book_name" "author" year_published "ISBN" [copies]
```

If the book is successfully added, the output will be:

```
Book added successfully.
```

Example:
    
```
add_book "Harry Potter and Philospher's Stone" "JK Rowling" 1998 "9780743273565" 5
```

***Effect on Database***
- A new book entry is added to the `books` table in the database.

- Database output figure:

Before:
![](/images/add%20books%20before.png)

After:
![](/images/add%20books.png)

### Remove Book

The `remove_book` command is used to remove a book from the library database. The command takes in the following parameters:

- `book_name`: The name of the book to be removed.
- `author`: The author of the book.

The command is used as follows:

```
remove_book "book_name" "author"
```

If the book is successfully removed, the output will be:

```Book removed successfully.```

Example:

```
remove_book "Harry Potter and Philospher's Stone" "JK Rowling"
```

***Effect on Database***
- The book entry is removed from the `books` table in the database.

- Database output figure:

Before:
![](/images/add%20books.png)

After:
![](/images/add%20books%20before.png)

### Look Up Books

The `look_up_books` command is used to look up books in the library database. The command takes in the following optional parameters:

- `book_name`: The name of the book to look up.
- `author`: The author of the book to look up.
- `year_published`: The year the book was published.

The command is used as follows:

```
look_up_books [--book_name="book_name"] [--author="author"] [--year_published=year]
```

If the book is found, the output will be:

```
Book found:
{
    "book_name": "Harry Potter and Philospher's Stone",
    "author": "JK Rowling",
    "year_published": 1998,
    "ISBN": "9780743273565",
    "copies": 5
}
```

Example:

```
look_up_books --book_name="Harry Potter and Philospher's Stone"
```

***Effect on Database***
- No effect on the database.

### Search Books

The `search_books` command is used to search for books in the library database based on a keyword. The command takes in the following parameter:

- `keyword`: The keyword to search for in the book names and authors.

The command is used as follows:

```
search_books "keyword"
```

If books are found, the output will be:

```
Books found:
[
    Detail of the books found
]
```

Example:

```
search_books "dragon"
```

Output:
```
Books found:
{'id': 91, 'book_name': 'The Girl with the Dragon Tattoo', 'author': 'Stieg Larsson', 'year_published': 2005, 'ISBN': '9780307454546', 'copies': 10}
``` 

Image:
![](/images/search_books.png)

***Effect on Database***
- No effect on the database.


### Is Book Lent

The `is_book_lent` command is used to check if a book is currently lent out. The command takes in the following parameter:

- `book_name`: The name of the book to check.

The command is used as follows:

```
is_book_lent "book_name"
```

If the book is lent out, the output will be:

```
Available copies: 10
```

Example:

```
is_book_lent "The Girl with the Dragon Tattoo"
```

Output:

![](/images/lent_out.png)

***Effect on Database***
- No effect on the database.


### Group Books by Year

The `group_books_by_year` command is used to group books in the library database by the year they were published. The command takes no parameters.

The command is used as follows:

```
group_books_by_year
```

If books are found, the output will be:

![](/images/group_books_by_year.png)

### Lend Book

The `lend_book` command is used to lend a book to a borrower. The command takes in the following parameters:

- `book_name`: The name of the book to be lent.
- `borrower_name`: The name of the borrower.
- `borrowed_date`: The date the book was borrowed.
- `due_date`: The due date for returning the book.

The command is used as follows:

```
lend_book "book_name" "borrower_name" "borrowed_date" "due_date"
```

If the book is successfully lent, the output will be:

```Book lent successfully.```

Example:

```
lend_book "The War of the Worlds" "Saksham Thaman" "2024-10-01" "2021-10-15"
```

***Effect on Database***
- In the loan table, a new entry is added with the book lent to the borrower.

- Database output figure:

![](/images/lend_books.png)


### Get Return Date

The `get_return_date` command is used to get the return date of a book that has been lent out. The command takes in the following parameter:

- `book_name`: The name of the book to get the return date for.

The command is used as follows:

```
get_return_date "book_name"
```

If the book is found, the output will be:

```Return date: 2021-10-15```

Example:

```
get_return_date "The War of the Worlds"
```

![](/images/return%20date.png)


### Get Borrower Details

The `get_borrower_details` command is used to get the details of the borrowers who have lent books. The command takes no parameters.

The command is used as follows:

```
get_borrower_details
```

If borrowers are found, the output will be:

![](/images/borrowers%20details.png)


### Return Book

The `return_book` command is used to return a book that has been lent out. The command takes in the following parameters:

- `book_name`: The name of the book to be returned.
- `return_date`: The date the book was returned.

The command is used as follows:

```
return_book "book_name" "return_date"
```

If the book is successfully returned, the output will be:

```Book returned successfully.```

Example:

```
return_book "The War of the Worlds" "2021-10-15"
```

![](/images/return%20book.png)


***Effect on Database***
- The borrower entry has a return date updated.

![](/images/return%20date%20database.png)


### Generate Report

The `generate_report` command is used to generate a report of the books in the library database which were borrowed with the number of times. The command takes no parameters.

The command is used as follows:

```
generate_report
```

If the report is generated, the output will be:

![](/images/generate_report.png)

***Effect on Database***
- No effect on the database.

### View Book Availability

The `view_book_availability` command is used to view the availability of books in the library database. The command takes no parameters.

The command is used as follows:

```
view_book_availability
```

If the books are available, the output will be:

![](/images/books%20availability.png)

***Effect on Database***
- No effect on the database.


### Export Books

The `export_books` command is used to export the books in the library database to a CSV file. The command takes in the following parameter:

- `filename.csv`: The name of the CSV file to export the books to.

The command is used as follows:

```
export_books "filename.csv"
```

If the books are exported, the output will be:

```Books exported successfully.```

Example:

```
export_books "books.csv"
```

![](/images/csv%20file%20of%20books.png)

***Effect on Database***
- No effect on the database.


### View Overdue Books

The `view_overdue_books` command is used to view the books that are overdue. The command takes in the following parameter:

- `current_date`: The current date.

The command is used as follows:

```
view_overdue_books "current_date"
```

If there are no overdue, the output will be:

![](/images/no%20books%20overdue.png)

Else, the output will be the name of the overdue books and borrower details.

Example:
- Here the book was lent to Saksham Thaman on 2024-10-01 and the due date was 2024-10-15. So, the book is overdue.

```view_overdue_books "2024-12-03"```

![](/images/overdue%20books.png)


***Effect on Database***
- No effect on the database.

### Calculate Fines

The `calculate_fines` command is used to calculate the fines for overdue books. The command takes in the following parameters:

- `current_date`: The current date.
- `fine_per_day`: The fine per day for overdue books.

The command is used as follows:

```
calculate_fines "current_date" fine_per_day
```

If there are no overdue books, the output will be:
    
    ```No overdue books.```
    
Else, the output will be the total fine amount for all the overdue books and the fine per borrower.

Example:

Here we are setting to Rs 100 per day as fine.
```
calculate_fines "2024-12-03" 100
```

![](/images/calculate%20fines.png)

***Effect on Database***
- No effect on the database.


### Extend Due Date

The `extend_due_date` command is used to extend the due date of a book that has been lent out. The command takes in the following parameters:

- `book_name`: The name of the book to extend the due date for.
- `new_due_date`: The new due date for returning the book.

The command is used as follows:

```
extend_due_date "book_name" "new_due_date"
```

If the due date is successfully extended, the output will be:

```Due date extended successfully.```

Example:

```
extend_due_date "The War of the Worlds" "2021-10-30"
```

![](/images/extend%20due%20date.png)

***Effect on Database***
- The due date entry is updated in the loan table.

![](/images/extend%20due%20date%20database.png)


### Reserve Book

The `reserve_book` command is used to reserve a book in the library database. The command takes in the following parameters:

- `book_name`: The name of the book to reserve.
- `reserver_name`: The name of the reserver.
- `reservation_date`: The date the book was reserved.

The command is used as follows:

```
reserve_book "book_name" "reserver_name" "reservation_date"
```

If the book is successfully reserved, the output will be:

```Book reserved successfully.```

Example:

```
reserve_book "1984" "Saksham Thaman" "2024-11-11"
```

![](/images/reserve%20book.png)

***Effect on Database***

- A new entry is added to the `reservations` table in the database.

![](/images/reserve%20book%20database.png)


### View Reservations

The `view_reservations` command is used to view the reservations of books in the library database. The command takes no parameters.

The command is used as follows:

```view_reservations```

If the books are reserved, the output will be:

![](/images/view%20reservation.png)

***Effect on Database***

- No effect on the database.


### Cancel Reservation

The `cancel_reservation` command is used to cancel a reservation of a book in the library database. The command takes in the following parameters:

- `book_name`: The name of the book to cancel the reservation for.
- `reserver_name`: The name of the reserver.

The command is used as follows:

```
cancel_reservation "book_name" "reserver_name"
```

If the reservation is successfully cancelled, the output will be:

```Reservation cancelled successfully.```

Example:

```
cancel_reservation "1984" "Saksham Thaman"
```

![](/images/cancel%20reservation.png)

***Effect on Database***

- The reservation entry is removed from the `reservations` table in the database.

![](/images/cancel%20reservation%20database.png)

