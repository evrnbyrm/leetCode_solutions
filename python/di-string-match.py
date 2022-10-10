def diStringMatch(s):
    st = 0
    en = len(s)
    res = []
    for indicator in s:
        if (indicator == 'D'):
            res.append(en)
            en -= 1
        else:
            res.append(st)
            st += 1
    res.append(st)
    return res

inp = 'IDID'
print(diStringMatch(inp))