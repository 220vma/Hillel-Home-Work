import heapq

sorted_list = []
l = [5, 14, 3, 3, 90, 11, 2, 3, 9, 60, 27, 0]
print(f'Куча: {l}')

heapq.heapify(l)

while len(l) > 0:
    sorted_list.append(heapq.heappop(l))

print(f'Отсортированный список: {sorted_list}')