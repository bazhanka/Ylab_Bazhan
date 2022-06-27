def count_find_num(primesL, limit):
    res = []
    first = 1
    for i in primesL:
        first = first*i
    if first <= limit:
        res.append(first)
    else:
        return []
    ind = 0
    rind = 0
    while ind < len(primesL):
        n = res[rind]*primesL[ind]
        if n <= limit:
            rind+=1
            res.append(n)
            res.sort()
        else:
            ind+=1
            rind = 0
            continue
    return [len(res), max(res)]

primesL = [2, 5, 7]
limit = 500
print(count_find_num(primesL, limit))

primesL = [2, 3]
limit = 200
print(count_find_num(primesL, limit))
#[13, 192]

primesL = [2, 5]
limit = 200
print(count_find_num(primesL, limit))
#[8, 200]

primesL = [2, 3, 5]
limit = 500
print(count_find_num(primesL, limit))\
#[12, 480]

primesL = [2, 3, 5]
limit = 1000
print(count_find_num(primesL, limit))
#[19, 960]

primesL = [2, 3, 47]
limit = 200
print(count_find_num(primesL, limit))

