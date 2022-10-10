def romanToInt(s: str) -> int:
    romanDict = {
            'I':1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    romanToValues = [romanDict[x] for x in list(s)]
    l = len(romanToValues)
    total = 0
    for i in range(l):
        if (i < l-1):
            if (romanToValues[i] < romanToValues[i+1]):
                total -= romanToValues[i]
                continue
        total += romanToValues[i]
    return total

print(romanToInt('CCLXXX'))