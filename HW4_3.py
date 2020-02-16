import re

def lengthcheck(pw):
    if len(pw) > 4:
        return True
    else:
        return False

def isletterssmall(pw):
    regexp = r'[a-z]|[0-9]'
    for i in range(0, len(pw)):
        if re.match(regexp, pw[i]) is None:
            return False
    return True

def eL_uneD(pw): 
    countL = 0
    countD = 0
    for i in range(0, len(pw)):
        if pw[i].isdigit():
            countD+=1
        else:
            countL+=1
    if countL % 2 == 0:
        if countD % 2 == 1:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    pw = input("Введите пароль: ")
    if lengthcheck(pw):
        if isletterssmall(pw):
            if eL_uneD(pw):
                print("{} - хороший пароль".format(pw))
            else:
                print("Пароль должен быть с четным количеством букв и нечетным количеством цифр")
        else:
            print("Все буквы должны быть латинскими и маленькими")
    else:
        print("Пароль должен быть больше 4 символов")