import itertools
from itertools import *
from typing import Dict, List, Any, Union


def count_way(cor1,cor2):
    return ((cor2[0] - cor1[0]) ** 2 + (cor2[1] - cor1[1]) ** 2) ** 0.5
def salesman(*args):
    post = args[0]
    cities = [el for el in args[1::]]
    ways = []
    all_dc: Dict[Union[Union[float, int], Any], List[str]] = {}
    for c in itertools.permutations(cities,len(cities)):
        ind = 0
        way = []
        dc = []
        w1 = count_way(post, c[0])
        way.append(w1)
        dc.append(f'-> {c[0]} {w1}')
        while ind < len(c)-1:
            w2 = count_way(c[ind],c[ind+1])
            way.append(w2)
            dc.append(f'-> {c[ind+1]} {w2}')
            ind+=1
        w3 = count_way(c[-1],post)
        dc.append(f'-> {post} {w3}')
        way.append(w3)
        ways.append(sum(way))
        all_dc[sum(way)] = ' '.join(dc)
    return f' {post} {all_dc[min(ways)]} = {min(ways)}'


print(salesman((0,2),(2,5),(5,2),(6,6),(8,3)))