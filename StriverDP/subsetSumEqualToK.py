'''
https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954?leftPanelTab=1
'''
from os import *
from sys import *
from collections import *
from math import *
'''
4 4
1 1 1 1


1,0,0,0,0
1,1,0,0,0
1,1,1,0,0
1,0,0,0,0

1,1
nt = dp[0][1] = 0
t = dp[0][0] = 1
dp[1][1] = 1

1,2
nt= dp[0][2] = 0
t = dp[0][1] = 0
dp[1][2] = 0

1,3
nt = dp[0][3] = 0
t = dp[0][2] = 0
dp[1][3] = 0

1,4
nt = dp[0][4] = 0
t = dp[0][3] = 0
dp[1][4] = 0

2,1
nt = dp[1][1] = 1
dp[2][1] = 1

2,2
nt = dp[1][2] = 0
t = dp[1][1] = 1
dp[2][2] = 1

2,3
nt = dp[1][3] = 0
t = dp[1][2] = 0
dp[2][3] = 0

2,4
3,1


''' 

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
    
    
    

