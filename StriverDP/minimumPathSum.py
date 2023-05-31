'''
https://www.codingninjas.com/codestudio/problems/minimum-path-sum_985349?leftPanelTab=1
'''

from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)

def minSumPath(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [float('inf') for i in range(m)]
    for i in range(n):
        temp = dp.copy()
        for j in range(m):
            if(i == 0 and j == 0):
                dp[j] = grid[0][0]
            else:
                up = float('inf')
                left = float('inf')
                if(i>0): up = temp[j]
                if(j>0): left = dp[j-1]
                dp[j] = grid[i][j] + min(up,left)
                # print("tp",temp)
                # print("dp",dp)
    return dp[m-1]

# Main.
t = int(input())
while (t > 0):
    l = list(map(int, input().split()))
    n,m = l[0], l[1]
    grid = []
    for i in range(n):
        ll = list(map(int, input().split()))
        grid.append(ll)
    print(minSumPath(grid))
    t -= 1
