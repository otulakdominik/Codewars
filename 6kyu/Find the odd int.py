def find_it(seq):
    seq_dict = {}
    for i in seq:
        seq_dict.update({i: seq.count(i)})
    for i in seq_dict:
        if seq_dict[i] % 2 == 1:
            return i
