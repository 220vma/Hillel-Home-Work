import random
import string

def passGen(length):
    password = []
    letters = string.ascii_letters + "0123456789"
    for i in range(0, length):
        flag = random.randint(0, len(letters)-1)
        password.append(letters[flag])
    output = "".join(password)
    return output

if __name__ == "__main__":
    length = int(input("Введите длину пароля: "))
    if length == 0:
        exit()
    password = passGen(length)
    print(password)