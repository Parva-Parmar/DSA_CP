'''
https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003?leftPanelTab=1
'''
from typing import *

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[0]*4 for i in range(n)]
    def td(day:int, task:int):
        maxi = 0
        if(day == 0):
            for i in range(3):
                if(task != i):
                    maxi = max(maxi, points[day][i])
            return maxi

        if(dp[day][task]):
            return dp[day][task]
        point = 0
        for i in range(3):
            if(i != task):
                point = points[day][i] + td(day-1, i)
                maxi = max(maxi, point)
        dp[day][task] = maxi
        return maxi
    
    return td(n-1,3)
