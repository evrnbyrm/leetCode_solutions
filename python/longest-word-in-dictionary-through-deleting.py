def findLongestWord(s, dictionary):
    output = ''
    for w in dictionary:
        temp = s
        for c in range(len(w)):
            i = temp.find(w[c])
            if (i == -1):
                break
            elif (c == len(w)-1):
                if (len(w) > len(output) or (len(w) == len(output) and w < output)):
                    output = w
            temp = temp[i+1:]
    return output

s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
print(findLongestWord(s, dictionary))