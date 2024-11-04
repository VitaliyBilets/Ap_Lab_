
def equal_xo(a):

    count_x = 0
    count_o = 0

    for char in a:
        if char == 'x' or char == 'X':
            count_x += 1
        elif char == 'o' or char == 'O':
            count_o += 1

    return count_x == count_o


a = " ooxx "
print(equal_xo(a))