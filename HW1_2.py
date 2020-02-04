def dictswork():
    a = {'a': 1, 'b': 4, 't': 67}
    b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
    
    
    o = []
    aKeys = a.keys()
    for i in aKeys:
        if i in b.keys():
            o.append(i)
    print("Ключи которые есть в обоих словарях: {}".format(o))

    
    t = []
    bKeys = b.keys()
    for i in bKeys:
        if i not in a.keys():
            t.append(i)
    print("Ключи которые есть только в словаре b, но нет в а: {}".format(t))

    
    p = {}
    for i in aKeys:
        if i in b.keys():
            p[i] = a[i] + b[i]
        else:
            p[i] = a[i]
    for i in bKeys:
        if i not in a.keys():
            p[i] = b[i]
    print("Одинаковые ключи суммируются: {}".format(p))

if __name__ == "__main__":
    dictswork()