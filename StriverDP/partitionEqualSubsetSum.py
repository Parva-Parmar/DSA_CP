'''
https://www.codingninjas.com/codestudio/problems/partition-equal-subset-sum_892980?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
'''

from os import *
from sys import *
from collections import *
from math import *


def subsetSumToK(n, k, arr):
    dp = [[0]*(k+1) for i in range(n)]
    for i in range(n):
        dp[i][0] = 1
    try:
        dp[0][arr[0]] = 1
    except:
        pass
    for ind in range(1,n):
        for target in range(1,k+1):
            # print(ind,target)
            # print(dp)
            notTake = dp[ind-1][target]
            take = 0
            if(arr[ind] <= target):
                take = dp[ind-1][target-arr[ind]]
            dp[ind][target] = take or notTake
    
    return dp[n-1][k]
    


def canPartition(arr, n):
    totalSum = sum(arr)
    if(totalSum % 2 != 0):
        return False
    return subsetSumToK(n, totalSum//2, arr)
