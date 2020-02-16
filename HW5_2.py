import random

a = int(input("Введите длину списка: "))

l = [random.randint(0, 100) for x in range(a)]
l.sort()

print(f'Ваш список: {l}')

mid = l[(a-1)//2] if a % 2 != 0 else (l[(a-1)//2] + l[a//2])/2
print(f'Медиана этого списка: {mid}')