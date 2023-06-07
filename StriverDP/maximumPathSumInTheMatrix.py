'''
https://www.codingninjas.com/codestudio/problems/maximum-path-sum-in-the-matrix_797998?source=youtube&campaign=striver_dp_videos&leftPanelTab=1
'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = matrix[0]
    curr = [0 for i in range(m)]

    for i in range(1,n):
        dn,rd,ld = -1*float('inf'),-1*float('inf'),-1*float('inf')
        for j in range(m):
            if(j>0): ld = dp[j-1] 
            if(j<m-1): rd = dp[j+1]
            dn = dp[j]
            curr[j] = matrix[i][j] + max(ld,rd,dn)
        
        dp = curr.copy()
        
    return max(dp)


#   taking inpit using fast I/O
def takeInput() :
    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix=[list(map(int, stdin.readline().strip().split(" "))) for row in range(n)]

    return matrix, n, m


#   main
T = int(input())
while (T > 0):
    T -= 1
    matrix, n, m = takeInput()
    print(getMaxPathSum(matrix))
