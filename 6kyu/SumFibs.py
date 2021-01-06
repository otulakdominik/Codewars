def sum_fibs(n):
    a = 0
    b = 1
    c = 0
    sum = 0
    for i in range(n):
        a = b
        b = c
        c = a + b
        if c % 2 == 0:
            sum += c
    return sum
