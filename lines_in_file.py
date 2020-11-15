''' 
Посчитать количество строк в файле и количество слов и символов в каждой строке
 
В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.
'''

def symbol_lines(file):
    lines = 0  #counter for lines
    for i in file:
        lines += 1
        print(i)
        word = 0 #counter for words
        for j in i:
            if j == ' ': #looking for words count by space. At the end +1
                word += 1
        print('symbols =', len(i), 'words =', word + 1)
    print('lines =', lines)

if __name__ == '__main__':
    textFile = open(r'tex.txt')
    symbol_lines(textFile)
    textFile.close()
