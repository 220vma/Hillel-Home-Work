def reverseWords(inputString):
    l = inputString.split(" ")
    for i in range(0, len(l)):
        l[i] = l[i][::-1]
    reversedWords = " ".join(l)
    return reversedWords

if __name__ == "__main__":
    inputSrting = input("Введите Вашу строку: ")
    rW = reverseWords(inputSrting)
    print(rW)