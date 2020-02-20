s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = int(input("Введите шаг: "))

while len(s) >= w:
    l = s[0:w]
    print(l)
    s = s[w:]

print(s)
