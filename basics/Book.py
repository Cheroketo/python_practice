from datetime import datetime


class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def info(self):
        print(f'Название книги - {self.name}\nНазвание автора - {self.author}\nГод издания - {self.year}')

    def is_old(self):
        return datetime.now().year-self.year > 50

book_1 = Book('Мастер и маргарите', 'Булгаков', 1920)

book_1.info()
print(book_1.is_old())