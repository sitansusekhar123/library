import mysql.connector
from mysql.connector import Error

# Connect to the MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='library',
            user='sitansu',
            password='mysql'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

# Look up books based on book name, author, or year
def look_up_books(book_name=None, author=None, year_published=None):
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM books_table WHERE 1=1"
        params = []

        if book_name:
            query += " AND book_name = %s"
            params.append(book_name)
        if author:
            query += " AND author = %s"
            params.append(author)
        if year_published:
            query += " AND year_published = %s"
            params.append(year_published)

        cursor.execute(query, params)
        results = cursor.fetchall()
        for row in results:
            print(row)
    finally:
        connection.close()

# Check if a specific book is currently lent out
def is_book_lent(book_id):
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT * FROM borrower_table
            WHERE book_id = %s AND return_date IS NULL
        """
        cursor.execute(query, (book_id,))
        result = cursor.fetchone()
        
        if result:
            print("Book is currently lent out.")
            print(result)
        else:
            print("Book is available.")
    finally:
        connection.close()

# Check the return date for a lent book
def get_return_date(book_id):
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT return_date FROM borrower_table
            WHERE book_id = %s AND return_date IS NOT NULL
            ORDER BY borrowed_date DESC LIMIT 1
        """
        cursor.execute(query, (book_id,))
        result = cursor.fetchone()
        
        if result:
            print("Return date:", result['return_date'])
        else:
            print("No return date found; the book may not be lent.")
    finally:
        connection.close()

# Function to get all books ordered by name or author
def get_books_ordered(order_by='name'):
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        if order_by == 'name':
            query = "SELECT * FROM books_table ORDER BY book_name ASC"
        elif order_by == 'author':
            query = "SELECT * FROM books_table ORDER BY author ASC"
        else:
            print("Invalid order_by value. Use 'name' or 'author'.")
            return
        
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    finally:
        connection.close()

# Function to group all books by year of publication
def group_books_by_year():
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT year_published, GROUP_CONCAT(book_name SEPARATOR ', ') AS books FROM books_table GROUP BY year_published"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"Year: {row['year_published']} - Books: {row['books']}")
    finally:
        connection.close()

# Function to get names of borrowers and the books they borrowed
def get_borrower_details():
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT borrower_table.borrower_name, books_table.book_name, borrower_table.borrowed_date, borrower_table.return_date
            FROM borrower_table
            JOIN books_table ON borrower_table.book_id = books_table.id
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    finally:
        connection.close()

# Function to get return date based on book name
def get_return_date_by_name(book_name):
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT borrower_table.return_date FROM borrower_table
            JOIN books_table ON borrower_table.book_id = books_table.id
            WHERE books_table.book_name = %s AND borrower_table.return_date IS NOT NULL
            ORDER BY borrower_table.borrowed_date DESC LIMIT 1
        """
        cursor.execute(query, (book_name,))
        result = cursor.fetchone()
        
        if result:
            print("Return date:", result['return_date'])
        else:
            print("No return date found; the book may not be lent.")
    finally:
        connection.close()

# Function to check if a book is lent out based on the book name
def is_book_lent_by_name(book_name):
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT borrower_table.borrower_name, borrower_table.borrowed_date FROM borrower_table
            JOIN books_table ON borrower_table.book_id = books_table.id
            WHERE books_table.book_name = %s AND borrower_table.return_date IS NULL
        """
        cursor.execute(query, (book_name,))
        result = cursor.fetchone()
        
        if result:
            print("Book is currently lent out to:", result['borrower_name'])
            print("Borrowed date:", result['borrowed_date'])
        else:
            print("Book is available.")
    finally:
        connection.close()

# Function to add a new book to the catalog
def add_book(book_name, author, year_published, ISBN):
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor()
        # Check if the book already exists
        check_query = "SELECT * FROM books_table WHERE book_name = %s AND author = %s"
        cursor.execute(check_query, (book_name, author))
        if cursor.fetchone():
            print("Book already exists in the catalog.")
            return
        
        # Insert new book
        insert_query = "INSERT INTO books_table (book_name, author, year_published, ISBN) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (book_name, author, year_published, ISBN))
        connection.commit()
        print("Book added successfully.")
    finally:
        connection.close()

# Function to remove a book from the catalog
def remove_book(book_name, author):
    connection = connect_to_db()
    if not connection:
        return
    
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM books_table WHERE book_name = %s AND author = %s"
        cursor.execute(delete_query, (book_name, author))
        if cursor.rowcount > 0:
            connection.commit()
            print("Book removed successfully.")
        else:
            print("Book not found in the catalog.")
    finally:
        connection.close()