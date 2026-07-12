books = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter Book Name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in books:
                print(book)

    elif choice == "3":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")