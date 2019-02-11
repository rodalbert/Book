from book import Book

class LibraryBook(Book):
    
    def __init__(self, title, author, inventory):
        super().__init__(title, author)
        self.inventory = inventory
        self.borrowers = []
    
    def check_out(self, name):
        if self.inventory < 1:
            print("Sorry, not available.")
            return 
        self.inventory -= 1
        self.borrowers.append(name)

    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Inventory Remaining: {self.inventory}")
        print(f"Borrowers: {', '.join(self.borrowers)}")


