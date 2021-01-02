def time_convert(num):
    hour = 0
    if num < 0:
        return "00:00"
    while num >= 60:
        num -= 60
        hour += 1
    if hour < 10 and num < 10:
        text = '0' + str(hour) + ':' + '0' + str(num)
    elif hour < 10 and num > 10:
        text = '0' + str(hour) + ':' + str(num)
    elif hour >= 10 and num < 10:
        text = str(hour) + ':' + '0' + str(num)
    else:
        text = str(hour) + ':' + str(num)
    print(text)
    return text
