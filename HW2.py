def symbol():
    s = "spam and eggs or eggs with spam"
    slist = list(s)
    sdict = {}
    a = 0
    for i in range(0, len(slist)):
        sdict[slist[i]] = 0
    for i in range(0, len(slist)):
        if slist[i] in slist:
            a = sdict[slist[i]] + 1
        sdict[slist[i]] = a
    return(sdict)

print(symbol())