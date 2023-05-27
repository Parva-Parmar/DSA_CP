/*
https://www.codingninjas.com/codestudio/problems/total-unique-paths_1081470?leftPanelTab=0
*/
#include <bits/stdc++.h> 
int uniquePaths(int m, int n) {
	int N = n+m-2;
	int R = n-1;
	double result = 1.0;
	for(int i = 1 ; i <= R ; i++){
		result = result*(N-R+i)/i;
	}
	return (int)result;
}
