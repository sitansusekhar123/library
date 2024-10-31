import argparse
import sys
from mysql.connector import Error
from library import *

# Assuming the previous functions are defined above or imported from a separate module

def parse_command(command_input):
    parser = argparse.ArgumentParser(description="Library Management CLI", prog='')
    subparsers = parser.add_subparsers(dest="command", help="Library commands")

    # Add book
    parser_add = subparsers.add_parser("add_book", help="Add a new book to the catalog")
    parser_add.add_argument("book_name", type=str, help="Name of the book")
    parser_add.add_argument("author", type=str, help="Author of the book")
    parser_add.add_argument("year_published", type=int, help="Year of publication")
    parser_add.add_argument("ISBN", type=str, help="ISBN of the book")

    # Remove book
    parser_remove = subparsers.add_parser("remove_book", help="Remove a book from the catalog")
    parser_remove.add_argument("book_name", type=str, help="Name of the book")
    parser_remove.add_argument("author", type=str, help="Author of the book")

    # Look up books
    parser_lookup = subparsers.add_parser("look_up_books", help="Look up books")
    parser_lookup.add_argument("--book_name", type=str, help="Name of the book")
    parser_lookup.add_argument("--author", type=str, help="Author of the book")
    parser_lookup.add_argument("--year_published", type=int, help="Year of publication")

    # Check if book is lent
    parser_lent = subparsers.add_parser("is_book_lent", help="Check if a book is lent out")
    parser_lent.add_argument("book_id", type=int, help="ID of the book")

    # Get return date
    parser_return = subparsers.add_parser("get_return_date", help="Get return date for a lent book")
    parser_return.add_argument("book_id", type=int, help="ID of the book")

    # Get books ordered
    parser_order = subparsers.add_parser("get_books_ordered", help="Get all books in alphabetical order")
    parser_order.add_argument("order_by", choices=["name", "author"], help="Order by 'name' or 'author'")

    # Group books by year
    parser_group = subparsers.add_parser("group_books_by_year", help="Group all books by year of publication")

    # Get borrower details
    parser_borrowers = subparsers.add_parser("get_borrower_details", help="Get names of borrowers and the books they borrowed")

    # Get return date by book name
    parser_return_name = subparsers.add_parser("get_return_date_by_name", help="Get return date based on book name")
    parser_return_name.add_argument("book_name", type=str, help="Name of the book")

    # Check if book is lent by name
    parser_lent_name = subparsers.add_parser("is_book_lent_by_name", help="Check if a book is lent out by name")
    parser_lent_name.add_argument("book_name", type=str, help="Name of the book")

    # Parse the input command
    args = parser.parse_args(command_input)
    return args

def main():
    print("Welcome to the Library Management CLI. Type 'quit' to exit.")
    
    while True:
        command_input = input("Enter command: ").strip().split()
        
        if command_input[0].lower() == "quit":
            print("Exiting the Library Management CLI.")
            break

        try:
            args = parse_command(command_input)
            if args.command == "add_book":
                add_book(args.book_name, args.author, args.year_published, args.ISBN)
            elif args.command == "remove_book":
                remove_book(args.book_name, args.author)
            elif args.command == "look_up_books":
                look_up_books(args.book_name, args.author, args.year_published)
            elif args.command == "is_book_lent":
                is_book_lent(args.book_id)
            elif args.command == "get_return_date":
                get_return_date(args.book_id)
            elif args.command == "get_books_ordered":
                get_books_ordered(args.order_by)
            elif args.command == "group_books_by_year":
                group_books_by_year()
            elif args.command == "get_borrower_details":
                get_borrower_details()
            elif args.command == "get_return_date_by_name":
                get_return_date_by_name(args.book_name)
            elif args.command == "is_book_lent_by_name":
                is_book_lent_by_name(args.book_name)
            else:
                print("Unknown command. Type 'quit' to exit or 'help' for options.")
        except SystemExit:
            print("Invalid command or arguments. Try again.")

if __name__ == "__main__":
    main()
