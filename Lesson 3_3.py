students = [['Krishna', 67, 68, 69], ['Arjun', 70, 98, 63], ['Malika', 52, 56, 60]]
key_students = []

for i in range(len(students)):
    d = dict([('Имя судента', students[i][0]), ('Физика', students[i][1]), ('Математика', students[i][2]), ('Химия', students[i][3])])
    key_students.append(d)
    
print(f'Группа: {key_students}')

name = str(input('Введите имя студента: '))
total = 0

for i in range(len(key_students)):
    if name in list(key_students[i].values()):
        total = (key_students[i]['Физика'] + key_students[i]['Математика'] + key_students[i]['Химия']) / 3

print(f'Ср арифм студента {name} : {total}')