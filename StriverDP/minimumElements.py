'''
https://www.codingninjas.com/codestudio/problems/minimum-elements_3843091?leftPanelTab=1
'''

from os import *
from sys import *
from collections import *
from math import *

from typing import List

def minimumElements(num: List[int], x: int) -> int:
    m = 10**9
    n = len(num)
    curr, prev = [0]*(x+1), [0]*(x+1)

    # base case
    for i in range(x+1):
        if(i%num[0] == 0):
            prev[i] = i // num[0]
        else:
            prev[i] = m
    
    for i in range(1,n):
        for T in range(1,x+1):
            notTake = prev[T]
            take = m
            if(num[i]<=T):
                take = 1 + curr[T - num[i]]
            
            curr[T] = min(take, notTake)
        
        prev = curr.copy()
    
    if(prev[x] >= m):
        return -1
    return prev[x]
