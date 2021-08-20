from classes import Book

class TutorialBook(Book):
    """This class will illustrate inheritance."""
    def __init__(self, name, author, price, num_of_projects, tech_stacks_covered) -> None:
        super().__init__(name, author, price)
        self.projects_count = num_of_projects
        self.topics = tech_stacks_covered
    
    def book_detail(self):
        """Exploring method overriding"""
        res_str = 'Book name: %s \nAuthor: %s \nProjects: %s \nTopics: %s'
        res_str = res_str % (self.name, self.author, self.projects_count, self.topics)
        print(res_str)


print(
    TutorialBook(*['Learn Python', 'Tareq', 500, 15, ['python', 'django', 'pillow', 'automation']])
)