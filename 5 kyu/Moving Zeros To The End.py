def move_zeros(array):
    cond = len(array)
    i = 0
    count_0 = 0
    while i < cond:
        if array[i] == 0 and array[i] is not False:
            array += [array.pop(i)]
            i -= 1
            count_0 += 1
        i += 1
        if count_0 + i == cond:
            break
    return array
