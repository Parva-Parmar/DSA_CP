'''
https://www.codingninjas.com/codestudio/problems/total-unique-paths_1081470?leftPanelTab=3
'''
from os import *
from sys import *
from collections import *
from math import *

def uniquePaths(m, n):
	m,n = int(m),int(n)
	dp = [1] * m
	for i in range(1, n):
		for j in range(1, m):
			dp[j] += dp[j-1]
	return dp[-1]
