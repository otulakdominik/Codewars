def filter_long_words(sentence, n):
    new_sentence = sentence.split()
    n_sentence = []
    for i in new_sentence:
        if len(i) > n:
            n_sentence.append(i)
    return n_sentence
