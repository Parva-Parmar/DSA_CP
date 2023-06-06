/*
https://www.codingninjas.com/codestudio/problems/triangle_1229398?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
*/
#include <bits/stdc++.h> 
int minimumPathSum(vector<vector<int>>& triangle, int n){
	vector<vector<int>> dp(n,vector<int>(n,0));
    dp[n-1] = triangle[n-1];
    for(int i = n-2 ; i >= 0 ; i--){
        for(int j = i ; j>=0 ; j--){
            int d = triangle[i][j] + dp[i+1][j];
            int diag = triangle[i][j] + dp[i+1][j+1];
            dp[i][j] = min(d,diag);
        }
    }
    return dp[0][0];
}
