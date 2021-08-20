from books_store import books


class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def description(self):
        desc = f"{self.name} by {self.author} - {self.price}"
        print(desc) 
    
    def __repr__(self):
        return self.name
    
    def __str__(self) -> str:
        return f'{self.name} by {self.author}'


if __name__ == '__main__':
    organized_books = []
    for book in books:
        book_obj = Book(**book)
        organized_books.append(book_obj)

    print(organized_books)