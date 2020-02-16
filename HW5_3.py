list_objects = [1, 'one', 'two', 3.0, 4j, 5j, 3, 2, 12., 17, [1,2], {1:1}]
count = {}
max_count = 1
max_index = ''

for _ in list_objects:
    if str(type(_)) not in list(count.keys()):
        count.update({str(type(_)) : 1})
    else:
        count[str(type(_))]+=1
        if count[str(type(_))] > max_count:
            max_count = count[str(type(_))]
            max_index = str(type(_))


print(f'Самый частый используемый тип данных в списке {list_objects}:')
print(max_index, ':')
for x in range(len(list_objects)):
    if str(type(list_objects[x])) == max_index:
        print(list_objects[x])