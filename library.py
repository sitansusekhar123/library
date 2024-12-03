import mysql.connector
from mysql.connector import Error
from datetime import datetime
import csv

# Function to connect to the MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='library',
            user='root',  # Replace with your MySQL username
            password='mysql',  # Replace with your MySQL password
            use_pure=True
        )
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

# Function to add a new book to the catalog (supports multiple copies)
def add_book(book_name, author, year_published, ISBN, copies=1):
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor()
        # Check if the book already exists
        check_query = "SELECT id FROM books WHERE book_name = %s AND author = %s"
        cursor.execute(check_query, (book_name, author))
        result = cursor.fetchone()
        if result:
            # Update the number of copies
            update_query = "UPDATE books SET copies = copies + %s WHERE id = %s"
            cursor.execute(update_query, (copies, result[0]))
            print(f"Added {copies} more copies to existing book.")
        else:
            # Insert new book
            insert_query = "INSERT INTO books (book_name, author, year_published, ISBN, copies) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (book_name, author, year_published, ISBN, copies))
            print("Book added successfully.")
        connection.commit()
    except Error as e:
        print("Failed to add book:", e)
    finally:
        connection.close()

# Function to remove a book from the catalog
def remove_book(book_name, author):
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM books WHERE book_name = %s AND author = %s"
        cursor.execute(delete_query, (book_name, author))
        if cursor.rowcount > 0:
            connection.commit()
            print("Book removed successfully.")
        else:
            print("Book not found in the catalog.")
    except Error as e:
        print("Failed to remove book:", e)
    finally:
        connection.close()

# Function to look up books based on criteria
def look_up_books(book_name=None, author=None, year_published=None):
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM books WHERE 1=1"
        params = []
        if book_name:
            query += " AND book_name LIKE %s"
            params.append(f"%{book_name}%")
        if author:
            query += " AND author LIKE %s"
            params.append(f"%{author}%")
        if year_published:
            query += " AND year_published = %s"
            params.append(year_published)
        cursor.execute(query, params)
        results = cursor.fetchall()
        if results:
            for book in results:
                print(book)
        else:
            print("No books found matching the criteria.")
    except Error as e:
        print("Failed to look up books:", e)
    finally:
        connection.close()

# Function to search books by partial name or author
def search_books(keyword):
    look_up_books(book_name=keyword)

# Function to check if a book is lent out
def is_book_lent(book_name):
    connection = connect_to_db()
    if not connection:
        return False
    try:
        cursor = connection.cursor()
        # Get book ID and copies
        book_query = "SELECT id, copies FROM books WHERE book_name = %s"
        cursor.execute(book_query, (book_name,))
        book = cursor.fetchone()
        if not book:
            print("Book not found in the catalog.")
            return False
        book_id, copies = book
        # Count lent copies
        loan_query = "SELECT COUNT(*) FROM loans WHERE book_id = %s AND return_date IS NULL"
        cursor.execute(loan_query, (book_id,))
        lent_count = cursor.fetchone()[0]
        available_copies = copies - lent_count
        if available_copies <= 0:
            print("All copies are currently lent out.")
            return True
        else:
            print(f"Available copies: {available_copies}")
            return False
    except Error as e:
        print("Failed to check book status:", e)
        return False
    finally:
        connection.close()

# Function to get the return date for a lent book
def get_return_date(book_name):
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor(dictionary=True)
        loan_query = """
            SELECT due_date FROM loans
            JOIN books ON loans.book_id = books.id
            WHERE books.book_name = %s AND loans.return_date IS NULL
            LIMIT 1
        """
        cursor.execute(loan_query, (book_name,))
        loan = cursor.fetchone()
        if loan:
            print(f"Return date: {loan['due_date']}")
        else:
            print("No active loan record found for this book.")
    except Error as e:
        print("Failed to get return date:", e)
    finally:
        connection.close()

# Function to group books by year of publication
def group_books_by_year():
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor()
        query = "SELECT year_published, GROUP_CONCAT(book_name SEPARATOR ', ') AS books FROM books GROUP BY year_published"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"Year: {row[0]} - Books: {row[1]}")
    except Error as e:
        print("Failed to group books by year:", e)
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
            SELECT loans.borrower_name, books.book_name, loans.borrowed_date, loans.due_date, loans.return_date
            FROM loans
            JOIN books ON loans.book_id = books.id
        """
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            for loan in results:
                print(loan)
        else:
            print("No loans have been made.")
    except Error as e:
        print("Failed to get borrower details:", e)
    finally:
        connection.close()

# Function to lend a book to a borrower
def lend_book(book_name, borrower_name, borrowed_date_str, due_date_str):
    connection = connect_to_db()
    if not connection:
        return
    try:
        borrowed_date = datetime.strptime(borrowed_date_str, "%Y-%m-%d").date()
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        cursor = connection.cursor()
        # Get book ID and copies
        book_query = "SELECT id, copies FROM books WHERE book_name = %s"
        cursor.execute(book_query, (book_name,))
        book = cursor.fetchone()
        if not book:
            print("Book not found in the catalog.")
            return
        book_id, copies = book
        # Count lent copies
        loan_query = "SELECT COUNT(*) FROM loans WHERE book_id = %s AND return_date IS NULL"
        cursor.execute(loan_query, (book_id,))
        lent_count = cursor.fetchone()[0]
        if lent_count >= copies:
            print("All copies are currently lent out.")
            return
        # Create loan record
        insert_query = "INSERT INTO loans (book_id, borrower_name, borrowed_date, due_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (book_id, borrower_name, borrowed_date, due_date))
        connection.commit()
        print("Book lent out successfully.")
    except Error as e:
        print("Failed to lend book:", e)
    finally:
        connection.close()

# Function to return a book
def return_book(book_name, return_date_str):
    connection = connect_to_db()
    if not connection:
        return
    try:
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
        cursor = connection.cursor()
        # Find the active loan
        loan_query = """
            SELECT loans.id FROM loans
            JOIN books ON loans.book_id = books.id
            WHERE books.book_name = %s AND loans.return_date IS NULL
            LIMIT 1
        """
        cursor.execute(loan_query, (book_name,))
        loan = cursor.fetchone()
        if loan:
            loan_id = loan[0]
            update_query = "UPDATE loans SET return_date = %s WHERE id = %s"
            cursor.execute(update_query, (return_date, loan_id))
            connection.commit()
            print("Book returned successfully.")
        else:
            print("Loan record not found or book already returned.")
    except Error as e:
        print("Failed to return book:", e)
    finally:
        connection.close()

# Function to view all overdue books
def view_overdue_books(current_date_str):
    connection = connect_to_db()
    if not connection:
        return
    try:
        current_date = datetime.strptime(current_date_str, "%Y-%m-%d").date()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT loans.borrower_name, books.book_name, loans.due_date FROM loans
            JOIN books ON loans.book_id = books.id
            WHERE loans.due_date < %s AND loans.return_date IS NULL
        """
        cursor.execute(query, (current_date,))
        results = cursor.fetchall()
        if results:
            for loan in results:
                print(f"Overdue Book: {loan['book_name']}, Borrower: {loan['borrower_name']}, Due Date: {loan['due_date']}")
        else:
            print("No overdue books.")
    except Error as e:
        print("Failed to view overdue books:", e)
    finally:
        connection.close()

# Function to calculate and display overdue fines
def calculate_fines(current_date_str, fine_per_day):
    connection = connect_to_db()
    if not connection:
        return
    try:
        current_date = datetime.strptime(current_date_str, "%Y-%m-%d").date()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT loans.borrower_name, books.book_name, loans.due_date FROM loans
            JOIN books ON loans.book_id = books.id
            WHERE loans.due_date < %s AND loans.return_date IS NULL
        """
        cursor.execute(query, (current_date,))
        results = cursor.fetchall()
        total_fines = 0
        for loan in results:
            days_overdue = (current_date - loan['due_date']).days
            fine = days_overdue * fine_per_day
            total_fines += fine
            print(f"Borrower: {loan['borrower_name']}, Book: {loan['book_name']}, Fine: Rs. {fine:.2f}")
        print(f"Total Fines: ${total_fines:.2f}")
    except Error as e:
        print("Failed to calculate fines:", e)
    finally:
        connection.close()

# Function to extend the due date of a borrowed book
def extend_due_date(book_name, new_due_date_str):
    connection = connect_to_db()
    if not connection:
        return
    try:
        new_due_date = datetime.strptime(new_due_date_str, "%Y-%m-%d").date()
        cursor = connection.cursor()
        # Find the active loan
        loan_query = """
            SELECT loans.id FROM loans
            JOIN books ON loans.book_id = books.id
            WHERE books.book_name = %s AND loans.return_date IS NULL
            LIMIT 1
        """
        cursor.execute(loan_query, (book_name,))
        loan = cursor.fetchone()
        if loan:
            loan_id = loan[0]
            update_query = "UPDATE loans SET due_date = %s WHERE id = %s"
            cursor.execute(update_query, (new_due_date, loan_id))
            connection.commit()
            print("Due date extended successfully.")
        else:
            print("Loan record not found or book already returned.")
    except Error as e:
        print("Failed to extend due date:", e)
    finally:
        connection.close()

# Function to reserve a book
def reserve_book(book_name, reserver_name, reservation_date_str):
    connection = connect_to_db()
    if not connection:
        return
    try:
        reservation_date = datetime.strptime(reservation_date_str, "%Y-%m-%d").date()
        cursor = connection.cursor()
        # Get book ID
        book_query = "SELECT id FROM books WHERE book_name = %s"
        cursor.execute(book_query, (book_name,))
        book = cursor.fetchone()
        if not book:
            print("Book not found in the catalog.")
            return
        book_id = book[0]
        # Create reservation
        insert_query = "INSERT INTO reservations (book_id, reserver_name, reservation_date) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (book_id, reserver_name, reservation_date))
        connection.commit()
        print("Book reserved successfully.")
    except Error as e:
        print("Failed to reserve book:", e)
    finally:
        connection.close()

# Function to cancel a reservation
def cancel_reservation(book_name, reserver_name):
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor()
        # Get book ID
        book_query = "SELECT id FROM books WHERE book_name = %s"
        cursor.execute(book_query, (book_name,))
        book = cursor.fetchone()
        if not book:
            print("Book not found in the catalog.")
            return
        book_id = book[0]
        # Delete reservation
        delete_query = "DELETE FROM reservations WHERE book_id = %s AND reserver_name = %s"
        cursor.execute(delete_query, (book_id, reserver_name))
        if cursor.rowcount > 0:
            connection.commit()
            print("Reservation cancelled successfully.")
        else:
            print("Reservation not found.")
    except Error as e:
        print("Failed to cancel reservation:", e)
    finally:
        connection.close()

# Function to view all reservations
def view_reservations():
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT reservations.reserver_name, books.book_name, reservations.reservation_date
            FROM reservations
            JOIN books ON reservations.book_id = books.id
        """
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            for res in results:
                print(f"Reserver: {res['reserver_name']}, Book: {res['book_name']}, Reservation Date: {res['reservation_date']}")
        else:
            print("No reservations found.")
    except Error as e:
        print("Failed to view reservations:", e)
    finally:
        connection.close()

# Function to view availability of all books
def view_book_availability():
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor()
        query = """
            SELECT books.book_name, books.copies - IFNULL(lent_count, 0) AS available_copies
            FROM books
            LEFT JOIN (
                SELECT book_id, COUNT(*) AS lent_count
                FROM loans
                WHERE return_date IS NULL
                GROUP BY book_id
            ) AS loaned_books ON books.id = loaned_books.book_id
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for book_name, available_copies in results:
            print(f"Book: {book_name}, Available Copies: {available_copies}")
    except Error as e:
        print("Failed to view book availability:", e)
    finally:
        connection.close()

# Function to generate reports (e.g., most borrowed books)
def generate_report():
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor()
        query = """
            SELECT books.book_name, COUNT(loans.id) AS borrow_count
            FROM loans
            JOIN books ON loans.book_id = books.id
            GROUP BY books.book_name
            ORDER BY borrow_count DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("Most Borrowed Books:")
        for book_name, count in results:
            print(f"{book_name}: {count} times")
    except Error as e:
        print("Failed to generate report:", e)
    finally:
        connection.close()
        
# New function to export book details to a CSV file
def export_books_to_csv(filename):
    connection = connect_to_db()
    if not connection:
        return
    try:
        cursor = connection.cursor()
        query = "SELECT id, book_name, author, year_published, ISBN, copies FROM books"
        cursor.execute(query)
        books = cursor.fetchall()
        headers = ['ID', 'Book Name', 'Author', 'Year Published', 'ISBN', 'Copies']

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(headers)
            for book in books:
                csvwriter.writerow(book)
        print(f"Books exported successfully to {filename}.")
    except Error as e:
        print("Failed to export books:", e)
    except IOError as e:
        print("I/O error:", e)
    finally:
        connection.close()