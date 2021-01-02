def who_took_the_car_key(message):
    name = ''
    for i in message:
        name += chr(int(i, 2))
    return name
