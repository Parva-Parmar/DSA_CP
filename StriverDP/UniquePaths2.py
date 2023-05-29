'''
https://www.codingninjas.com/codestudio/problems/maze-obstacles_977241?leftPanelTab=1
'''
MOD = 10**9 + 7
def mazeObstacles(n, m, mat):
    global MOD
    dp = [[0]*(m) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if(mat[i][j] == -1):
                continue
            elif(i == 0 and j == 0):
                dp[i][j] = 1;
                continue
            if(i-1<0):
                dp[i][j] = dp[i][j-1]
            elif(j-1<0):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # print(dp)
    return dp[n-1][m-1]%MOD
