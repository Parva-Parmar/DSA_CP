/*
https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003?leftPanelTab=1
*/

int ninjaTraining(int n, vector<vector<int>> &points)
{
  vector<int> dp(4,0);
  vector<int> temp(4,0);
  dp[0] = max(points[0][1],points[0][2]);
  dp[1] = max(points[0][0],points[0][2]);
  dp[2] = max(points[0][0],points[0][1]);
  dp[3] = max(points[0][0],max(points[0][1],points[0][2]));
  for(int day = 1 ; day < n ; day++){
    for(int last = 0 ; last < 4 ; last++){
      temp[last] = 0;

      for(int task = 0 ; task<3 ; task++){
        if(task!= last){
          temp[last] = max(temp[last],points[day][task] + dp[task]);
        }
      }
    }
    dp = temp;
  }
  return dp[3];
} 
 
