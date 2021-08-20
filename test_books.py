"""Test Book & TutorialBook classes."""
from classes import Book


class TestBook:
    """
    With the help of testing, we'll know how unfortunate behavior our Book class
    can expose. We then can try to refactor our code.
    """
    wrong_params = ['Tareq', 20, 'Learning Programming']
    correct_params = {'name': 'Design Patterns', 'author': 'Gang of four', 'price': 4500}

    PASSING_FLAG = '=== PASSING ==='
    def test_init_with_invalid_params(self, wrong_params):
        """
        We expect, wrong params should not return a book object if it's params aren't valid.
        But, this test case will pass and we'll get a book anyway!
        Do we need to refactor our Book class? decission is up to you.
        """
        try:
            book = Book(*wrong_params)
            msg = f'{book} | book crated successfully!'
            print(self.PASSING_FLAG, msg)
            return True
        except Exception as e:
            print(e)
            return False

    def run(self):
        self.test_init_with_invalid_params(self.wrong_params)


book_test_suit = TestBook()
book_test_suit.run()