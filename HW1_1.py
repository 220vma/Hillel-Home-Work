
a = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2,7, 43, 54, 13]
print("Максимальное значение в списке:", max(a), ", а его индекс:", a.index(max(a)))
print("Минимальное значение в списке:", min(a), ", а его индекс:", a.index(min(a)))


a = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2,7, 43, 54, 13]
output = {1:(), 2:(), 3:()}
for i in a:
    f = i
    t = 0
    for j in range(0, len(a)):
        if f == a[j]:
            t +=1
    cand = (i, t)
    try:
        if cand[1] >= output[1][1] and cand[0] != output[1][0]:
            output[3] = output[2]
            output[2] = output[1]
            output[1] = cand
    except:
        output[1] = cand 
print("3-и самых часто встречаемых элемента: ", output)


a = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2,7, 43, 54, 13]

b = [] 
for i in a:
    if i in b:
        continue
    else:
        b.append(i)

a = set(a)
print("Порядок не сохраняется:", a)
print("Порядок сохраняется:", b)

