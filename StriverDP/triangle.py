'''
https://www.codingninjas.com/codestudio/problems/triangle_1229398?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
'''

from os import *
from sys import *
from collections import *
from math import *

def minimumPathSum(triangle, n):
    front = triangle[-1]
    for i in reversed(range(n-1)):
        curr = [0 for k in range(i+1)]
        for j in reversed(range(i+1)):
            up = front[j]
            diag = front[j+1]
            curr[j] = triangle[i][j] + min(up, diag)
        front = curr.copy()
    return front[0]
