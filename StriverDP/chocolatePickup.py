'''
https://www.codingninjas.com/codestudio/problems/ninja-and-his-friends_3125885?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
'''

from os import *
from sys import *
from collections import *
from math import *

from typing import List


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])

    dp = []
    for i in range(n):
        dp.append([])
        for j in range(m):
            dp[i].append([])
            for k in range(m):
                dp[i][j].append(-1)

    dj = [-1, 0, 1]
    
    for i in range(m):
        for j in range(m):
            if(i == j):
                dp[0][i][j] = grid[0][i]
            else:
                dp[0][i][j] = grid[0][i] + grid[0][j]

    for i in range(1,n):
        for j1 in range(m):
            for j2 in range(m):
                if(dp[i][j1][j2] != -1):
                    continue
                for k in dj:
                    maxi = -1
                    for l in dj:
                        if(j1+k < 0 or j1+k >= m or j2+l < 0 or j2+l >= m):
                            continue
                        if(j1+k == j2+l):
                            maxi = max(maxi, grid[i][j1+k] + dp[i-1][j1+k][j2+l])
                        else:
                            maxi = max(maxi, grid[i][j1+k] + grid[i][j2+l] + dp[i-1][j1+k][j2+l])
                        dp[i][j1+k][j2+l] = maxi
    
    return dp[-1][-1][0]
