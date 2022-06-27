import itertools

def bananas(s) -> set:
    result = set()
    if all ((s.count('b') >= 1, s.count('a') >= 3, s.count('n') >= 2)):
        if s == 'banana':
            result.add(s)
        n = len(s)-6
        all_ind = list(itertools.combinations(range(0,len(s)), n))
        for l in all_ind:
            s_list = [el for el in s]
            for el in l:
                s_list[el] = '-'
                news = ''.join(el for el in s_list if el != '-')
                if news == 'banana':
                    res = ''.join(s_list)
                    result.add(res)
    return result

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

