from isbnlib import is_isbn13

class Book:
    BOOKS = {}

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.__class__.BOOKS[self.ISBN] = {"title": self.title, "author": self.author}

    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("The book must have a title.")
        else:
            self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("The book must have an author name.")
        else:
            self._author = value

    @property
    def ISBN(self):
        return self._ISBN
    
    @ISBN.setter
    def ISBN(self, value):
        value = str(value)
        if not is_isbn13(value):
            raise ValueError("Invalid ISBN: Must be a valid 13-digit number.")
        if value in self.__class__.BOOKS:
            raise ValueError("ISBN must be unique.")
        else:
            self._ISBN = value

    def get_books(self):
        return self.__class__.BOOKS
    
    def __str__(self):
        return f"This library has {len(self.__class__.BOOKS)} books. Details: {self.get_books()}"