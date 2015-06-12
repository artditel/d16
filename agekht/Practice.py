#Хроматическое число

matrix = []        #matrix - матрица, clr[i] - набор цветов для i-той вершины, b - цвета для каждой вершины (массив чисел [цветов], которым уже покрасили вершины)

with open("input.txt") as f:                                    #считываем граф
    s = f.readline()
    while s:
        matrix.append([int(c) for c in s.split()])
        s = f.readline()

count_colours = 1                                             
b = [0] * len(matrix)
clr = [range(2, count_colours + 2) for i in range (0, len(matrix))]   #каждой цифре соответствует цвет


def dying(clr, matrix, i, count_colours, b):
    while i < len(matrix):
        clr[i] = range(2, count_colours + 2)
        for j in range(0, len(matrix)):                               #анализируем соседние вершины на предмет использования того же цвета
            a = matrix[i][j]
            if a > 1 and matrix[i][j] in clr[i]:
               clr[i] = delete(clr[i], matrix[i][j])      #???        #убираем использованные цвета и оставляем доступные (вопрос по delete)
        if clr[i] != []:                                         #если остались цвета для раскраски, красим и вершину и храним оставшиеся 
            b[i] = clr[i][0] - 1
            for c in range(i + 1, len(matrix)):
                if matrix[c][i] >= 1:
                    matrix[c][i] = clr[i][0]
            i += 1
        else:                                                    #если не осталось цветов - возвращаемся назад
            clr, matrix, i, count_colours, b = upper(clr, matrix, i, count_colours, b)
    return b
 

def upper (clr, matrix, i, count_colours, b):
    clr[i] = range(2, count_colours + 2) 
    i -= 1
    if len(clr[i]) > 1:                                          #если у предыдущей вершины есть цвета - перекрашиваем
        clr[i].pop(0)
        b[i] = clr[i][0] - 1
        for c in range(i + 1, len(matrix)):
            if matrix[c][i] >= 1:
                matrix[c][i] = clr[i][0]
        i += 1
        return (clr, matrix, i, count_colours, b)
    else:                                                        #если нет, то либо возвращаемся назад, либо красим заново с ещё одним цветом
        if i == 0:
            count_colours += 1
            b = [0] * len(matrix)
            clr = [range(2, count_colours + 2)] * len(matrix)
            return (clr, matrix, 0, count_colours, b)
        else:
            return upper(clr, matrix, i, count_colours, b)


def delete(lst, d):
    for i in range (0, len(lst)):
        if lst[c] == d:
            lst = lst[0:c] + lst[(c + 1):len(lst)]
            return lst

print dying(clr, matrix, 0, count_colours, b)

#Хроматический многочлен; он и есть f
matrix1 = matrix
f = 0

def removing(clr, matrix, matrix1, i, count_colours, b):
    while matrix == matrix1:
        for j in range (len(matrix)):
            if matrix[i][j] == 1:
                matrix1[i][j] == 0
                matrix1[j][i] == 0


def contraction(clr, matrix, matrix1, i, count_colours, b):
    for k in range (len(matrix)):







def chrompol(clr, matrix, matrix1, i, count_colours, b):
    for i in range(len(matrix)):
        if matrix[i][i] == 1:
            f = 0
        else:
            f = 
