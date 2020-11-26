'''
1. Класс библиотека
    Поля:
        - список книг (list Book)
        - список должников (list People)

    Методы:
        - Добавить книгу
        - Удалить книгу
        - Отдать книгу посетителю
        - Принять книгу от посетителя

        - Вывести список всех книг
        - Вывести список книг в библиотеке (в наличии)
        - Вывести списк книг, которые не в наличии

        - Отсортировать список книг по названию, автору, году издания (lambda будет плюсом)

2. Класс книга
    Поля:
        - ID
        - Название
        - Автор
        - Год издания
        - ??? (этот параметр нужен!!!)

3. Класс People
    - ???

    Методы:
        ???
'''


class SuBook:

    def __init__(self, name, author, year, id_b, borrow=False):

        self.name = name
        self.author = author
        self.year = year
        self.id_b = id_b
        self.borrow = borrow

    def __repr__(self):
        return f'{self.name},{self.author},{self.year},{self.id_b},{self.borrow}'

    def __str__(self):
        return f'{self.name},{self.author},{self.year},{self.id_b},{self.borrow}'


class SuLibrary:
    def __init__(self, list_book: list, man=None):
        self.list_book = list_book
        self.man = man

    def add_book(self, add_book):
        self.list_book.append(add_book)

    def remove_book(self, id_remove_book: int):
        j = 1
        for i in self.list_book:
            if id_remove_book == j:
                self.list_book.remove(i)
            j += 1

    def print_all_books(self):
        book = self.list_book
        print('%-50s%-20s%-5s%-2s' % ('Name', 'Author', 'Year', 'id'))
        for i in book:
            book_temp = str(i)
            book_temp = book_temp.replace("[", "")
            book_temp = book_temp.replace("]", "")
            book_temp = book_temp.split(',')
            print('%-50s%-20s%-5s%-2s' % (book_temp[0], book_temp[1], book_temp[2], book_temp[3]))

    def give_book(self, id_book, id_man):
        for i in self.list_book:
            print(i)
            j = str(i)
            j = j.split(',')
            print(j[4])
            # if j[3] == id_book and j[4] == 'False':
            #     SuLibrary.remove_book(id_book)


            print(i[3])








class SuPeople:
    def __init__(self, name, surname, id_p, debt=None):
        self.name = name
        self.surname = surname
        self.id_p = id_p
        self.debt = debt

    def __repr__(self):
        return f'{self.name},{self.surname},{self.id_p}'

    def __str__(self):
        return f'{self.name},{self.surname},{self.id_p}'


if __name__ == "__main__":
    book1 = SuBook(name='Harry Potter & blah blah', author='Rolling', year=1995, id_b=1)
    book2 = SuBook(name='Charley & chocolate factory ', author='Dahll', year=1970, id_b=2)

    myLib = SuLibrary([book1, book2])

    man1 = SuPeople(name='Bob', surname='Stragolsky', id_p=1)

    book3 = SuBook(name='TestTestTest', author='TestTest', year=1980, id_b=3)

    myLib.add_book(book3)
    # myLib.remove_book(3)

    # SuLibrary.print_all_books(myLib)

    myLib.give_book(3, 1)

