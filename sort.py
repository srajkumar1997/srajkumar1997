def sortBySecond(val):
    return val[1]
list_of_seq = [(10, 12, 14), (2, 4, 6), (5, 15, 25), (3, 6)]
list_of_seq.sort(key = sortBySecond)
print(list_of_seq)
