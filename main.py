from mysql.connector import Error
from library import *
import shlex  # Import shlex module for proper parsing of user input

# CLI that runs until 'quit' is entered
def library_cli():
    print("Welcome to the Library Management CLI. Type 'help' to see available commands.")
    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == 'quit':
            print("Exiting the Library Management CLI.")
            break
        elif user_input.lower() == 'help':
            print("""
Available commands:
- add_book "book_name" "author" year_published "ISBN" [copies]
- remove_book "book_name" "author"
- look_up_books [--book_name="book_name"] [--author="author"] [--year_published=year]
- search_books "keyword"
- is_book_lent "book_name"
- get_return_date "book_name"
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
""")
        else:
            # Use shlex.split to properly parse quoted strings
            try:
                args = shlex.split(user_input)
            except ValueError as e:
                print(f"Error parsing input: {e}")
                continue
            if not args:
                continue
            command = args[0]
            if command == 'add_book':
                if len(args) < 5:
                    print("Usage: add_book \"book_name\" \"author\" year_published \"ISBN\" [copies]")
                else:
                    copies = int(args[5]) if len(args) > 5 else 1
                    add_book(args[1], args[2], int(args[3]), args[4], copies)
            elif command == 'remove_book':
                if len(args) != 3:
                    print("Usage: remove_book \"book_name\" \"author\"")
                else:
                    remove_book(args[1], args[2])
            elif command == 'look_up_books':
                kwargs = {}
                for arg in args[1:]:
                    if arg.startswith('--book_name='):
                        kwargs['book_name'] = arg.split('=', 1)[1]
                    elif arg.startswith('--author='):
                        kwargs['author'] = arg.split('=', 1)[1]
                    elif arg.startswith('--year_published='):
                        kwargs['year_published'] = int(arg.split('=', 1)[1])
                look_up_books(**kwargs)
            elif command == 'search_books':
                if len(args) != 2:
                    print("Usage: search_books \"keyword\"")
                else:
                    search_books(args[1])
            elif command == 'is_book_lent':
                if len(args) != 2:
                    print("Usage: is_book_lent \"book_name\"")
                else:
                    is_book_lent(args[1])
            elif command == 'get_return_date':
                if len(args) != 2:
                    print("Usage: get_return_date \"book_name\"")
                else:
                    get_return_date(args[1])
            elif command == 'group_books_by_year':
                group_books_by_year()
            elif command == 'get_borrower_details':
                get_borrower_details()
            elif command == 'lend_book':
                if len(args) != 5:
                    print("Usage: lend_book \"book_name\" \"borrower_name\" \"borrowed_date\" \"due_date\"")
                else:
                    lend_book(args[1], args[2], args[3], args[4])
            elif command == 'return_book':
                if len(args) != 3:
                    print("Usage: return_book \"book_name\" \"return_date\"")
                else:
                    return_book(args[1], args[2])
            elif command == 'view_overdue_books':
                if len(args) != 2:
                    print("Usage: view_overdue_books \"current_date\"")
                else:
                    view_overdue_books(args[1])
            elif command == 'calculate_fines':
                if len(args) != 3:
                    print("Usage: calculate_fines \"current_date\" fine_per_day")
                else:
                    calculate_fines(args[1], float(args[2]))
            elif command == 'extend_due_date':
                if len(args) != 3:
                    print("Usage: extend_due_date \"book_name\" \"new_due_date\"")
                else:
                    extend_due_date(args[1], args[2])
            elif command == 'reserve_book':
                if len(args) != 4:
                    print("Usage: reserve_book \"book_name\" \"reserver_name\" \"reservation_date\"")
                else:
                    reserve_book(args[1], args[2], args[3])
            elif command == 'cancel_reservation':
                if len(args) != 3:
                    print("Usage: cancel_reservation \"book_name\" \"reserver_name\"")
                else:
                    cancel_reservation(args[1], args[2])
            elif command == 'view_reservations':
                view_reservations()
            elif command == 'view_book_availability':
                view_book_availability()
            elif command == 'generate_report':
                generate_report()
                
            elif command == 'export_books':
                if len(args) != 2:
                    print("Usage: export_books \"filename.csv\"")
                else:
                    export_books_to_csv(args[1])
                    
            else:
                print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    library_cli()