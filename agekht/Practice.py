#Хроматическое число

x = []        #x - матрица, clr[i] - набор цветов для i-той вершины, b - цвета для каждой вершины (массив чисел [цветов], которым уже покрасили вершины)

with open("input.txt") as f:                                    #считываем граф
    s = f.readline()
    while s:
        x.append([int(c) for c in s.split()])
        s = f.readline()

count_colours = 1                                             
b = [0] * len(x)
clr = [range(2, count_colours + 2) for i in range (0, len(x))]   #каждой цифре соответствует цвет


def dying(clr, x, i, count_colours, b):
    while i < len(x):
        clr[i] = range(2, count_colours + 2)
        for j in range(0, len(x)):                               #анализируем соседние вершины на предмет использования того же цвета
            a = x[i][j]
            if a > 1 and x[i][j] in clr[i]:
               clr[i] = delete(clr[i], x[i][j])      #???        #убираем использованные цвета и оставляем доступные (вопрос по delete)
        if clr[i] != []:                                         #если остались цвета для раскраски, красим и вершину и храним оставшиеся 
            b[i] = clr[i][0] - 1
            for c in range(i + 1, len(x)):
                if x[c][i] >= 1:
                    x[c][i] = clr[i][0]
            i += 1
        else:                                                    #если не осталось цветов - возвращаемся назад
            clr, x, i, count_colours, b = upper(clr, x, i, count_colours, b)
    return b
 

def upper (clr, x, i, count_colours, b):
    clr[i] = range(2, count_colours + 2) 
    i -= 1
    if len(clr[i]) > 1:                                          #если у предыдущей вершины есть цвета - перекрашиваем
        clr[i].pop(0)
        b[i] = clr[i][0] - 1
        for c in range(i + 1, len(x)):
            if x[c][i] >= 1:
                x[c][i] = clr[i][0]
        i += 1
        return (clr, x, i, count_colours, b)
    else:                                                        #если нет, то либо возвращаемся назад, либо красим заново с ещё одним цветом
        if i == 0:
            count_colours += 1
            b = [0] * len(x)
            clr = [range(2, count_colours + 2)] * len(x)
            return (clr, x, 0, count_colours, b)
        else:
            return upper(clr, x, i, count_colours, b)


def delete(lst, d):
    for i in range (0, len(lst)):
        if lst[c] == d:
            lst = lst[0:c] + lst[(c + 1):len(lst)]
            return lst

print dying(clr, x, 0, count_colours, b)
