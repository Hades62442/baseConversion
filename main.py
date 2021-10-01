# a program to convert numbers from base x to base y
# x, y, and the number to convert are given by the user

def getNumbers():
    print("Enter number to convert: ")
    number = input()
    print("Enter what base the number to convert is in: ")
    baseNumber = input()
    print("Enter what base you want to convert the number to: ")
    convBaseNumber = input()

    return number, baseNumber, convBaseNumber


def convertNumber(number, baseNumber, convBaseNumber):
    if int(baseNumber) == 10:
        finalNum = base10ToNewBase(number, convBaseNumber)
    elif int(convBaseNumber) == 10:
        finalNum = newBaseToBase10(number, baseNumber) 
    elif baseNumber == convBaseNumber:
        return number
    else:
        baseTenNum = newBaseToBase10(number, baseNumber)
        finalNum = base10ToNewBase(baseTenNum, convBaseNumber)

    return finalNum


def base10ToNewBase(number, newBase):
    rems = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    a = (-1, -1)
    num = int(number)

    while a[0] != 0:
        a = divmod(num, int(newBase))
        rems.append(a[1])
        num = a[0]

    finalNum = ''
    for i in range(len(rems)-1, -1, -1):
        if str(rems[i]) in digits:
            finalNum = finalNum + str(rems[i])
        else:
            extra = rems[i] - 9
            finalNum = finalNum + str(chr(64+extra))
        
    return finalNum


def newBaseToBase10(number, oldBase):
    digitsInNum = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(len(number)-1, -1, -1):
        digitsInNum.append(str(number[i]))

    for i in range(len(digitsInNum)):
        if digitsInNum[i] in digits:
            pass
        else:
            digitsInNum[i] = str(int(ord(digitsInNum[i])) - 55)

    finalNum = 0
    for i in range(len(digitsInNum)):
        finalNum += int(digitsInNum[i]) * (int(oldBase)**i)

    return finalNum


def main():
    number, baseNumber, convBaseNumber = getNumbers()
    finalNum = convertNumber(number, baseNumber, convBaseNumber)

    print(f"{number} in base {baseNumber} converted to base {convBaseNumber} is {finalNum}")


while True:
    if __name__ == "__main__":
        main()
