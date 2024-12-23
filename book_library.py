class BookLibrary:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, pages):
        self.books.append({"title": title, "author": author, "pages": pages})

    def list_books_with_index(self):
        result = ""
        for i, book in enumerate(self.books, 1):
            title, author, pages = book.values()
            result += f"{i}. {title} by {author}\n"
        return result

    def find_long_books(self, min_pages):
        return list(filter(lambda book: book["pages"] > min_pages, self.books))

    def average_pages(self):
        average =  list(map(lambda book: book["pages"], self.books))
        return sum(average) / len(average)


books = BookLibrary()
books.add_book("To Kill a Mockingbird", "Harper Lee", 200)
books.add_book("The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid ", 450)
books.add_book("The Fault in Our Stars", "John Green", 140)
books.add_book("The Alchemist", "Paulo Coelho ", 925)
books.add_book("The da Vinci Code", "Dan Brown ", 170)

print(books.list_books_with_index())
print(books.find_long_books(100))
print(books.average_pages())