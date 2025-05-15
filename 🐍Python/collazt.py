def collatz(x):
    while x != 1:
        if x % 2 > 0:
             x =((3 * x) + 1)
             list.append(x)
        else:
            x = (x / 2)
            list.append(x)
    return list

print(collatz())