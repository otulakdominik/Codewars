def christmas_tree(height):
    tree = ''
    first = True
    for i in range(1, height + 1):
        if first == False:
            tree += '\n'
            tree += ' ' * (height - i) + '*' * ((i * 2) - 1) + ' ' * (height - i)
        else:
            tree += ' ' * (height - i) + '*' + ' ' * (height - i)
            first = False

    return tree
