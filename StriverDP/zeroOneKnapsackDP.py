'''
https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542?source=youtube&campaign=striver_dp_videos&leftPanelTab=1
'''


from os import *
from sys import *
from collections import *
from math import *
from typing import List


def knapsack(weights: List[int], values: List[int], W:int, n:int) -> int:
    dp = [[0]*(W+1) for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

# inputs
T = int(input())
for _ in range(T):
    n = int(input())
    wt = list(map(int,input().split()))
    val = list(map(int,input().split()))
    W = int(input())

    print(knapsack(wt, val, W, n))
