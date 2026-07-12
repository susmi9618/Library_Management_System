books = []
try:
    with open("books.txt", "r") as file:
        books = file.read().splitlines()
except FileNotFoundError:
    pass

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Update Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter Book Name: ")
        books.append(book)
        with open("books.txt", "w") as file:
            file.write(book + "\n")
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in books:
                print(book)

    elif choice == "3":
        search = input("Enter Book Name to Search: ")
        if search in books:
            print("Book found!")
        else:
            print("Book not found!")

    elif choice == "4":
        delete_book = input("Enter Book Name to Delete: ")
        if delete_book in books:
            books.remove(delete_book)
            print("Book deleted successfully!")
        else:
            print("Book Not Found!")

    elif choice == "5":
        update_book = input("Enter Book Name to Update: ")
        if update_book in books:
            books.remove(update_book)
            new_book = input("Enter New Book Name: ")
            books.append(new_book)
            print("Book updated successfully!")
        else:
            print("Book Not Found!")

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")