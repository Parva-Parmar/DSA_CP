'''
https://www.codingninjas.com/codestudio/problems/ninja-and-his-friends_3125885?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
'''

from os import *
from sys import *
from collections import *
from math import *

from typing import List


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    front = [[0]*m for _ in range(m)]
    cur = [[0]*m for _ in range(m)]

    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                front[j1][j2] = grid[n-1][j1]
            else:
                front[j1][j2] = grid[n-1][j1] + grid[n-1][j2]

    for i in range(n-2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = -maxsize

                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]

                        if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
                            ans += int(-1e9)
                        else:
                            ans += front[j1 + di][j2 + dj]
                        maxi = max(ans, maxi)
            cur[j1][j2] = maxi
        front = cur.copy()

    return front[0][m-1]

