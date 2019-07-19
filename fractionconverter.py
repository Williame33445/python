def searchStr(string,target="."):
    for x in range(len(string)):
        if string[x] == target:
            return str(x)
            break

def floatToFraction(f):
    seperator = searchStr(str(f))
    if seperator ==  None:
        print(f)
    else:
        print(fractionCreator(str(f),int(seperator)))

def fractionCreator(string,seperator):
    fraction = fractionSimplifier(string,seperator)
    highestFactor = findHighestFactor(fraction[0],fraction[1])
    simplifiedNumerator = fraction[0] / highestFactor
    simplifiedDenominator = fraction[1] / highestFactor
    return str(int(simplifiedNumerator)) + " / " + str(int(simplifiedDenominator))

def fractionSimplifier(string,seperator):
    wholeNumber = string[:seperator]
    decimalNumber = string[seperator+1:]
    tempDenominator = 10 ** len(decimalNumber)
    tempNumerator = int(decimalNumber) + (int(wholeNumber) * tempDenominator)
    return [tempNumerator,tempDenominator]

def findHighestFactor(numerator,denominator):
    numeratorFactors = findFactors(numerator)
    denominatorFactors = findFactors(denominator)
    commanFactors = compareLists(numeratorFactors,denominatorFactors)
    return commanFactors[-1]

def findFactors(numb):
    factors = []
    for i in range(numb):
        if numb % (i+1) == 0:
            factors.append(i+1)
    return factors[1:-1]


def compareLists(listOne,listTwo):
    commonVariables = []
    for x in range(len(listOne)):
        for i in range(len(listTwo)):
            if listOne[x] == listTwo[i]:
                commonVariables.append(listOne[x])
    return commonVariables

floatToFraction(12.25)
