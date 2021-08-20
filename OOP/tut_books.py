from books import Book


class TutorialBook(Book):
    def __init__(self, n_of_projects, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_of_projects = n_of_projects


tut_book = TutorialBook(
    3, author='Book', name='Author', price=300
)
tut_book.description()
