

class SuBook:

    def __init__(self, name, author, year, idB, borrow=None):

        self.name = name
        self.author = author
        self.year = year
        self.idB = idB
        self.borrow = borrow

    def __repr__(self):
        return f'{self.name},{self.author},{self.year},{self.idB}'

    def __str__(self):
        return f'{self.name},{self.author},{self.year},{self.idB}'



class SuLibrary:
    def __init__(self, listBook:list):
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
        
            if idRemoveBook == j:
                self.listBook.remove(i)
            j += 1

    def printAllBooks(self):
        book = self.listBook
        print('%-50s%-20s%-5s%-2s' % ('Name', 'Author', 'Year', 'id'))
        for ij in book:
            bookT = str(ij)
            bookT = bookT.replace("[", "")
            bookT = bookT.replace("]", "")
            bookT = bookT.split(',')
            print('%-50s%-20s%-5s%-2s' % (bookT[0], bookT[1], bookT[2], bookT[3]))
    # def giveBook(self):
        


class SuPeople:
    def __init__(self, name, surname, age, debt=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.debt = debt


    def __repr__(self):
        return f'{self.name},{self.surname},{self.age}'

    def __str__(self):
        return f'{self.name},{self.surname},{self.age}'


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
