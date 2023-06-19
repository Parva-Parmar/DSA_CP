"""
https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
"""
from os import *
from sys import *
from collections import *
from math import *
from typing import List

## Read input as specified in the question.
## Print output as specified in the question.

def Knapsack(n: int,weight: List[int],values: List[int],maxCapacity: int) -> int:
    prev = [0]*(maxCapacity+1)  
    for x in range(weight[0],maxCapacity+1):
        prev[x] = val[0]

    for i in range(1,n):
        for w in reversed(range(maxCapacity+1)):
            notTake = prev[w]
            Take = -float('inf')
            if weight[i] <= w:
                Take =  values[i]+prev[w-weight[i]] 
            prev[w] = max(Take,notTake)
    return prev[maxCapacity]

T = int(input())
for _ in range(T):
    n = int(input())
    wt = list(map(int,input().split()))
    val = list(map(int,input().split()))
    W = int(input())
    print(Knapsack(n,wt,val,W))
