class Book:
    def __init__(self, name, author, price) -> None:
        self.name = name
        self.author = author
        self.price = price
    
    def __str__(self) -> str:
        return f'{self.name} by {self.author}'
    
    def __repr__(self) -> str:
        return f'{self.name} by {self.author}'


if __name__ == '__main__':
    books_raw = [
    {'name': 'Book1', 'author': 'Tareq', 'price': 100},
    {'name': 'Book2', 'author': 'John', 'price': 200},
    {'name': 'Book3', 'author': 'Alif', 'price': 150},
    ]

    books_obj = []

    for book in books_raw:
        books_obj.append(
            Book(**book)
        )


    for book_obj in books_obj:
        print(
            book_obj.name,
            book_obj.author,
            book_obj.price
        )


