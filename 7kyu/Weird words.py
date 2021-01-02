def next_letter(s):
    new_s = ''
    for i in s:
        if i == ' ' or ord(i) > 122 or ord(i) < 65:
            new_s += i
        else:
            if i == 'z':
                new_s += 'a'
            elif i == 'Z':
                new_s += 'A'
            else:
                new_s += chr(ord(i) + 1)
    return new_s
