#Хроматическое число

matrix = []        #matrix - матрица, clr[i] - набор цветов для i-той вершины, b - цвета для каждой вершины (массив чисел [цветов], которым уже покрасили вершины)

with open("input.txt") as f:                                    #считываем граф
    s = f.readline()
    while s:
        matrix.append([int(c) for c in s.split()])
        s = f.readline()

count_colours = 1                                                     #количество цветов, которым мы пытаемся покрасить граф
b = [0] * len(matrix)                                                 #список доступных цветов для каждой вершины
clr = [range(2, count_colours + 2) for i in range (0, len(matrix))]   #каждой цифре соответствует цвет


def dying(clr, matrix, i, count_colours, b):
    while i < len(matrix):
        clr[i] = list(range(2, count_colours + 2))
        for j in range(0, len(matrix)):                               #анализируем соседние вершины на предмет использования того же цвета
            a = matrix[i][j]
            if a > 1 and matrix[i][j] in clr[i]:
               clr[i] = delete(clr[i], matrix[i][j])                 #убираем использованные цвета и оставляем доступные 
        if clr[i] != []:                                             #если остались цвета для раскраски, красим и вершину и храним оставшиеся 
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
        if lst[i] == d:
            lst = lst[0:i] + lst[(i + 1):]
            return lst

a = (dying(clr, matrix, 0, count_colours, b))
print (a[4])
#count_colours - хроматическое число
#check

#Хроматический многочлен

matrix = []

with open("input.txt") as f:                                    #считываем граф
    s = f.readline()
    while s:
        matrix.append([int(c) for c in s.split()])
        s = f.readline()

coeff = [0] * (len(matrix) + 1)

class Poly:
    def __init__(self, coeff):
        self.coeff = coeff
        self.degree = len(coeff) - 1
    
    def __add__(self, other):
        (coeff1, coeff2) = (self.coeff, other.coeff)
        if (len(coeff1) > len(coeff2)):
            (coeff1, coeff2) = (coeff2, coeff1)
        coeff = [0] * len(coeff2)
        for j in range(len(coeff2)):
            coeff[j] = coeff2[j]
        for i in range(len(coeff1)):    
            coeff[i] = [coeff1[i] + coeff2[i]]
        return Poly(coeff)

    def __sub__(self, other):
        (coeff1, coeff2) = (self.coeff, other.coeff)
        if len(coeff1) > len(coeff2):
            coeff2 = coeff2 + [0] * (len(coeff1) - len(coeff2))
        coeff1 = coeff1 + [0] * (len(coeff2) - len(coeff1)) 
        coeff = [0] * len(coeff1)
        for i in range(len(coeff1)):
            coeff[i] = coeff1[i] - coeff2[i]
        return Poly(coeff)
        
    def __str__(self):
        nonZeros = ['(' + str(self.coeff[i]) + 'x^' \
                + str(i) + ')'\
                for i in range(self.degree + 1) \
                if self.coeff[i] != 0]
        nonZeros = nonZeros[::-1]
        if len(nonZeros) == 0:
            return str(0)
        else:
            nonZeros = ' + '.join(nonZeros)
            return (str(nonZeros))

def finding(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                return (i, j)
    return None

def removing(matrix, i, j):
    matrix1 = [matrix[i][:] for i in range(0, len(matrix))]    
    matrix1[i][j] = 0
    matrix1[j][i] = 0
    return (matrix1)    

def contraction(matrix, i, j):
    matrixc = [matrix[i][:] for i in range(0, len(matrix))]
    for l in range(len(matrix)):
        if matrixc[j][l] == 1:
            matrixc[i][l] = 1
            matrixc[l][i] = 1
    matrixc[i][i] = 0
    for k in range(len(matrix)):
        matrixc[k].pop(j)
    matrixc.pop(j)
    return (matrixc)


def calc_polynomial(matrix):
    if finding(matrix):
        i, j  = finding(matrix)
        return calc_polynomial(removing(matrix, i, j)) - calc_polynomial(contraction(matrix, i, j))
    else:
        coeff = [0] * len(matrix)
        coeff.append(1)
        x = Poly(coeff)
        return (x)

a = calc_polynomial(matrix)
print(a)
        
