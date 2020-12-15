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




class SuBook(dict):

    def __init__(self, name, author, year, id_b):
        self["name"] = name
        self["author"] = author
        self["year"] = year
        self["id_b"] = id_b

    def __repr__(self):
        return f'{self["name"]},{self["author"]},{self["year"]},{self["id_b"]}'

    def __str__(self):
        return f'{self["name"]},{self["author"]},{self["year"]},{self["id_b"]}'


class SuLibrary(dict):
    def __init__(self, list_book: list):
        self["list_book"] = list_book
        self["man"] = []

    def add_book(self, add_book):
        self["list_book"].append(add_book)

    def remove_book(self, id_remove_book: int):
        j = 1
        for i in self["list_book"]:
            if id_remove_book == j:
                self["list_book"].remove(i)
            j += 1

    def print_lib_books(self):
        book = self["list_book"]
        print('%40s' % 'Shelf of library')
        print('%-50s%-20s%-5s%-3s' % ('Name:', 'Author', 'Year', 'id'))
        for i in book:
            book_temp = str(i)
            book_temp = book_temp.replace("[", "")
            book_temp = book_temp.replace("]", "")
            book_temp = book_temp.split(',')
            print(f'{book_temp[0]:50}{book_temp[1]:20}{book_temp[2]:5}{book_temp[3]:3}')

    def give_book(self, mans, books):
        if books in self["list_book"]:
            if mans not in self["man"]:
                self["man"].append(mans)
            mans["debt"].append(books)
            books = str(books)
            books = books.split(',')
            j = books[3]
            self.remove_book(int(j))

    def take_book(self, mans, books):
        if books in mans.debt:
            mans["debt"].remove(books)
            self.add_book(books)

    def print_books_man(self):
        mans = self["man"]
        print('%40s' % 'Borrowed books')
        print('%-50s%-20s%-5s%-3s' % ('Name:', 'Author', 'Year', 'id'))
        k = ''
        for i in mans:
            book_temp = str(i)
            book_temp = book_temp.replace("[", "")
            book_temp = book_temp.replace("]", "")
            book_temp = book_temp.split(',')
            print(f'{book_temp[0]:50}{book_temp[1]:20}{book_temp[2]:5}{book_temp[3]:3}')


class SuPeople(dict):
    def __init__(self, name, surname, id_p):
        self["name"] = name
        self["surname"] = surname
        self["id_p"] = id_p
        self["debt"] = []

    def __repr__(self):
        return f'{self["name"]},{self["surname"]},{self["id_p"]},{self["debt"]}'

    def __str__(self):
        return f'{self["name"]},{self["surname"]},{self["id_p"]},{self["debt"]}'


if __name__ == "__main__":
    book1 = SuBook(name='Harry Potter & blah blah', author='Rolling', year=1995, id_b=1)
    book2 = SuBook(name='Charley & chocolate factory ', author='Dahll', year=1970, id_b=2)

    man1 = SuPeople(name='Rob', surname='Sapolsky', id_p=1)
    myLib = SuLibrary([book1, book2])
    book3 = SuBook(name='TestTestTest', author='TestTest', year=1980, id_b=3)

    myLib.add_book(book3)
    # myLib.remove_book(3)

    myLib.give_book(man1, book3)

    # myLib.take_book(man1, book3)
    man2 = SuPeople(name='Bob', surname='Ross', id_p=2)
    myLib.give_book(man2, book2)
    SuLibrary.print_lib_books(myLib)
    SuLibrary.print_books_man(myLib)
