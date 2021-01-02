def create_array_of_tiers(n):
    array = []
    tier = ''
    for i in str(n):
        tier += i
        array.append(tier)
    return array
