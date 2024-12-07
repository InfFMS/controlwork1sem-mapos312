for x in range(2020+1):
    y = 3**100 - x
    z = 0 #ввожу счетчик
    while y!=0:
        if y%3 == 0:
            z += 1
        y = y//3
    if z == 2:
        print(x)
        break