'''
Библиотека

Создать два класса:
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

    def __init__(self, name, author, year, idB, borrow=None):

        self.name = name
        self.author = author
        self.year = year
        self.idB = idB
        self.borrow = borrow

    def __repr__(self):
        return f'name - {self.name}, author - {self.author}, year - {self.year}, id - {self.idB}'

    def __str__(self):
        return f'name - {self.name}, author - {self.author}, year - {self.year}, id - {self.idB}'



class SuLibrary:
    def __init__(self, listBook:list, listPeople):
        self.listBook = listBook

    def __repr__(self):
        return f'{self.listBook}'

    def __str__(self):
        return f'{self.listBook}'

    def addBook(self, addBook):
        self.listBook.append(addBook)

    def removeBook(self, idRemoveBook:int):
        j = 1
        for i in self.listBook:
            print(i)
            if idRemoveBook == j:
                self.listBook.remove(i)
            j += 1

    def printAllBooks(self):
        book = self.listBook
        # print('%-30s%-15s%-5s%-2s' % ('Name', 'author', 'year', 'id'))
        for i in book:
            print(i)
    # def giveBook(self):
        


class SuPeople:
    def __init__(self, name, surname, age, debt=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.debt = debt


    def __repr__(self):
        return f'name - {self.name}, surname - {self.surname}, age - {self.age}'

    def __str__(self):
        return f'name - {self.name}, surname - {self.surname}, age - {self.age}'


if __name__ == "__main__":
    book1 = SuBook(name='Harry Potter & blah blah', author='Rolling', year=1995, idB=1)
    book2 = SuBook(name='Charley & chocolate factory ', author='Dahll', year=1970, idB=2)

    myLib = SuLibrary([book1, book2])

    man1 = SuPeople(name='Bob', surname='Stragolsky', age=37)

    book3 = SuBook(name='TestTestTest', author='TestTest', year=1980, idB=3)

    myLib.addBook(book3)

    # SuLibrary.printAllBooks(myLib)

    myLib.removeBook(3)

    SuLibrary.printAllBooks(myLib)
