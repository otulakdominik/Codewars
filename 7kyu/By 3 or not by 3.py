def divisible_by_three(st):
    a = list(st)
    sum = 0
    for i in a:
        sum += int(i)
    while sum > 0:
        sum -= 3
    if sum == 0:
        return True
    else:
        return False
