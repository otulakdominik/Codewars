def solution(s):
    tab_s = []
    a = ''
    for i in range(0, len(s), 2):
        try:
             a = s[i] + s[i+1]
        except:
            a = s[i] + '_'
        tab_s.append(a)
    return tab_s
