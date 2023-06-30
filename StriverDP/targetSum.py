'''
https://www.codingninjas.com/studio/problems/target-sum_4127362?source=youtube&campaign=striver_dp_videos&leftPanelTab=1
'''

from os import *
from sys import *
from collections import *
from math import *

from typing import List

def findWays(num: List[int], tar: int) -> int:
    n = len(num)
    dp = [[0]*(tar+1) for i in range(n)]
    if(num[0] == 0): 
        dp[0][0] = 2
    else: 
        dp[0][0] = 1
    if(num[0] != 0 and num[0] <= tar): 
        dp[0][num[0]] = 1


    for ind in range(1,n):
        for target in range(tar+1):
            notTake = dp[ind-1][target]
            take = 0
            if(num[ind] <= target):
                take = dp[ind-1][target-num[ind]]
            dp[ind][target] = (take + notTake)
    
    return dp[n-1][tar]

def countPartitions(n: int, d: int, arr: List[int]) -> int:
    totalSum = sum(arr)
    if((totalSum - d) % 2 == 1 or( totalSum - d )< 0): return 0
    return findWays(arr, (totalSum - d) // 2 )

def targetSum(arr: List[int], target: int) -> int:
    return int(countPartitions(len(arr), target, arr))


