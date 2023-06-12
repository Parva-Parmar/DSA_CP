/*
https://www.codingninjas.com/codestudio/problems/partition-equal-subset-sum_892980?source=youtube&campaign=striver_dp_videos&leftPanelTab=0
*/
bool subsetSumToK(int n, int k, vector<int> &arr) {
    vector<vector<bool>> dp(n,vector<bool>(k+1,false));
    for(int i = 0 ; i<n ; i++){
        dp[i][0] = true;
    }
    if(arr[0] < k){
        dp[0][arr[0]] = true;
    }
    for(int ind = 1 ; ind<n ; ind++){
        for(int target = 1 ; target <=k ; target++){
            bool notTake = dp[ind-1][target];
            bool take = false;
            if (arr[ind] <= target) {
              take = dp[ind - 1][target - arr[ind]];
            }
            dp[ind][target] = take||notTake;
        }
    }
    return dp[n-1][k];
}

bool canPartition(vector<int> &arr, int n)
{
	int totalsum = 0;
	for(int i = 0 ; i < n ; i++){
		totalsum += arr[i];
	}
	if(totalsum&1){
		return false;
	}
	int target = totalsum/2;
	return subsetSumToK(n, target, arr);

}
