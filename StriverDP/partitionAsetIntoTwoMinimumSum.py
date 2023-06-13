'''
https://www.codingninjas.com/codestudio/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def minSubsetSumDifference(arr, n):
    k = sum(arr)
    front = [0 for i in range(k+1)]
    curr = [0 for i in range(k+1)]
    front[0] = 1
    try:
        front[arr[0]] = 1
    except:
        pass

    for ind in range(1,n):
        front[0] = 1
        for target in range(1,k+1):
            notTake = front[target]
            take = 0
            if(arr[ind] <= target):
                take = front[target-arr[ind]]
            curr[target] = take or notTake
        front = curr.copy()
    ans = float('inf')
    flag = 1
    for i in range(k):
        if(front[i]):
            flag = 0
            ans = min(ans, abs(i-(k-i)))
    if(flag):
        ans = arr[0]
    return ans










# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = minSubsetSumDifference(arr, N)
    stdout.write(str(ans) + "\n")
    tc -= 1
