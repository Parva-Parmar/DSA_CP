'''
https://www.codingninjas.com/codestudio/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
'''

from os import *
from sys import *
from collections import *
from math import *

from typing import List

def findWays(num: List[int], tar: int) -> int:
    n = len(num)
    dp = [[0]*(tar+1) for i in range(n)]
    for i in range(n):
        dp[i][0] = 1
    try:
        dp[0][num[0]] = 1
    except:
        pass
    for ind in range(n):
        for target in range(tar+1):
            notTake = dp[ind-1][target]
            take = 0
            if(num[ind] <= target):
                take = dp[ind-1][target-num[ind]]
            dp[ind][target] = take + notTake
    
    return dp[n-1][tar]
