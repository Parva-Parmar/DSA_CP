/*
https://www.codingninjas.com/codestudio/problems/maximum-path-sum-in-the-matrix_797998?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
*/
#include <bits/stdc++.h> 

int getMaxPathSum(vector<vector<int>> &matrix)
{
    int n = matrix.size();
    int m = matrix[0].size();
    vector<int> dp(m,0);
    vector<int> curr(m,0);
    dp = matrix[0];
    
    for(int i = 1 ; i <n ; i++){
        int down = -1e8,right = -1e8,left = -1e8;
        for(int j = 0 ; j < m ; j++){
            down = matrix[i][j] +  dp[j];
            if(j>0){
                right = matrix[i][j] + dp[j-1];
            }
            if(j+1 < m){
                left = matrix[i][j] + dp[j+1];
            }
            curr[j] = max(down , max(right,left));
        }
        dp = curr;
    }
    int maxx = -1e8;
    for(int i = 0 ; i < m ; i++){
        maxx = max(maxx,dp[i]);
    }
    return maxx;
}
