class Library:
    BookName = ["Harry Potter", "The Hobbit", "The Alchemist", "The Lord of the Rings", "The Da Vinci Code", "The Great Gatsby", "The Catcher in the Rye"]
    TotalBooks = len(BookName)
    BookID = [1, 2, 3, 4, 5, 6, 7]

    def showAvailableBooks(self):
        print("\nAvailable Books are:\n")
        
        for name, book_id in zip(self.BookName, self.BookID):

            
            print(f"{name.ljust(30)} {str(book_id).rjust(5)}")

    def addBooks(self):
        book_name = input("Enter Name of the Book You want to add:\n")
        self.BookName.append(book_name)
        self.TotalBooks += 1
        self.BookID.append(self.TotalBooks)
        print(f"{book_name} added Successfully!")
        print(f"{self.TotalBooks} Books are added in the Library!")

    def Ask(self):
        print("\nPress 1 to Get a Book and 2 to add a Book")
        choice = int(input())
        if choice == 1:
            self.showAvailableBooks()
            print("\nEnter the Book ID to get the Book")
            book_id = int(input())
            if book_id in self.BookID:
                index = self.BookID.index(book_id)
                del self.BookID[index]
                del self.BookName[index]
                print("\nBook Issued Successfully")
            else:
                print("Invalid Book ID")
        elif choice == 2:
            self.addBooks()
        else:
            print("Invalid Input")


a = Library()
# a.showAvailableBooks()
a.Ask()
a.showAvailableBooks()

print(f"Total Books are: {a.TotalBooks}")
