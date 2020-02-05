def polyndrome(inputString):
    l = inputString
    middle = len(l) // 2
    backi = 0
    isPoly = False
    for i in range(0, middle):
        backi-=1
        if l[i] == l[backi]:
            if (i+1) == middle:
                isPoly = True
            continue
        else:
            break
    return isPoly

if __name__ == "__main__":
    inputString = input("Введите Вашу строку: ")
    isPoly = polyndrome(inputString)
    print("Является даная строка {} полиндромом? {}".format(inputString, isPoly))