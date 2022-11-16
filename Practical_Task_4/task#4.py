def greatcomdiv(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def reducfraction(numer, denom):
    return numer // greatcomdiv(numer, denom), denom // greatcomdiv(numer, denom)


print(reducfraction(6, 63))
