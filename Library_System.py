class Book:
    def __init__(self, title, author):
       
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
      
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Success: You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry: '{self.title}' is already borrowed.")

    def return_book(self):
        
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Success: '{self.title}' has been returned and is now available.")
        else:
            print(f"Notice: '{self.title}' was not checked out.")


book1 = Book("Diary of a Wimpy Kid", "Jeff Kinney")
book2 = Book("Charlie and the Chocolate Factory", "Roald Dahl")
book3 = Book("Esio Trot", "Roald Dahl")

print("--- Demonstrating Borrowing ---")
book1.borrow()
book2.borrow()
book3.borrow()

print("\n--- Demonstrating Returning ---")
book1.return_book()
book2.return_book()
book3.return_book()


    