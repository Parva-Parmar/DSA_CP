/*
https://codeforces.com/contest/1167/problem/B
*/

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define rev reverse
#define nl '\n'
#define flp(x,y) for(int i = x ; i < y ; ++i)
#define fln(x,y) for(int i = y ; i > x ; --i)
#define Motto_Hayakku ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define vi vector<long long int>
#define vb vector<bool>
#define vs vector<string>
#define pb push_back
#define rs(v,x) sort(v.begin(),v.end(),greater<x>())
#define MT make_tuple
#define MP make_pair
#define gv(i,n) get<n>(v[i])
#define maxe(v) max_element(v.begin(),v.end())
#define mine(v) min_element(v.begin(),v.end())
#define ff first
#define ss second
#define p(x) cout << x << "\n"
#define lp(x) cout << x << " " 
#define cout(v) for(auto &i : v) cout<<i<<" "; cout<<"\n"
#define sz(s) (long long)(s.size())
#define sp(n) cout<<setprecision(n)<<fixed;
#define in(v) for(auto &item : v) cin>>item;
#define inp(v) for(auto &item : v) cin>>item.ff>>item.ss;
#define YES cout << "YES" << "\n";
#define NO cout << "NO" << "\n";
#define Yes cout << "Yes" << "\n";
#define No cout << "No" << "\n";
 
#ifndef ONLINE_JUDGE
#define db(x)            cerr << #x <<" "; _print(x); cerr << endl;
#define gt(T)            cerr << "Case #" << T << ": " << endl;
#else
#define db(x)
#define gt(T)            
#endif
 
using namespace std;
typedef long long int ll;
typedef long double ld;
const int N = 1e5 + 1;
const int mod = 1e9 + 7;
 
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>

// using namespace __gnu_pbds;

// template <typename T>
// using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

 

/*
 
1. Think Greedy
2. Think Brute Force
3. Think solution in reverse order
4. Think DP [ check constraints carefully ]
5. Check base cases for DP and prove solution for Greedy
6. Think Graph 
 
*/

// bool srt(const pair<ll,ll> &a, const pair<ll,ll> &b){
//     if(a.ff!= b.ff){
//         return a.ff < b.ff;
//     }
//     else{
//         return b.ss > a.ss;
//     }
// }

// set<ll> printDivisors(ll n){set<ll> v;for (ll i=1; i<=sqrt(n); i++){if (n%i == 0){if (n/i == i)v.insert(i);else{v.insert(i);v.insert(n/i);}}}return v;}
 
// class Disjointset {
    
// public:
//     vector<ll> size,parent;
//     Disjointset(int n){
//         size.resize((n+1),1);
//         parent.resize(n+1);
//         iota(parent.begin(),parent.end(),0);
//     }
 
//     int findUpar(int node){
//         if(node == parent[node]){
//             return node;
//         }
//         return findUpar(parent[node]);
//     }
 
//     void unionBySize(int u , int v){
//         int ulp_u = findUpar(u);
//         int ulp_v = findUpar(v);
//         if(ulp_v == ulp_u){
//             return;
//         }
//         if(size[ulp_u]<size[ulp_v]){
//             parent[ulp_u] = ulp_v;
//             size[ulp_v] += size[ulp_u];
//         }
//         else{
//             parent[ulp_v] = ulp_u;
//             size[ulp_u] += size[ulp_v];
//         }
//     }
// };

// bool sortbysec(const pair<int,int> &a,const pair<int,int> &b)
// {
//     return (a.ss < b.ss);
// }

// ll modd = 998244353;
// const int NMAX = 2e5+5;
// vector<pair<ll,ll>> g[NMAX];

// void dfs(vector<ll> &dp,vector<ll> &id,ll parent){
//     for(auto it : g[parent]){
//         if(dp[it.ff] == 0){
//             dp[it.ff] = dp[parent] + (it.ss <= id[parent]);
//             id[it.ff] = it.ss;
//             dfs(dp,id,it.ff);
//         }
//     }
// }


int query(int a,int b)
{
	int x;
	printf("? %d %d",a,b);
    cout << endl;
	cin>>x;
	cout << endl;
	return x;
}

// int query(int a, int b)
// {
//     cout << "? " << a << " " << b << endl;
//     cout.flush();
//     int k;
//     cin >> k;
//     return k;
// }

void solve(){ 
    set<int> st({4,8,15,16,23,42});
    vector<int> nums = {4,8,15,16,23,42};
    vector<int> ans(6);
    map<int,pair<int,int>> mp;
    
    for(int i = 0 ; i < 6 ; i++){
        for(int j = i+1 ; j < 6 ; j++){
            int temp = nums[i]*nums[j];
            mp[temp] = {nums[i],nums[j]};
        }
    }
    
    vector<int> qrt(4);
    for(int i = 1 ; i <= 4 ; i++){
        qrt[i-1] = query(i,(i+1));
    }
    set<int> unq;
    
    pair<int,int> p1 = mp[qrt[0]];
    unq.insert(p1.ff);
    unq.insert(p1.ss);
    pair<int,int> p2 = mp[qrt[1]];
    
    if(unq.count(p2.ff)){
        unq.erase(p2.ff);
        ans[0] = *unq.begin();
        ans[1] = p2.ff;
        ans[2] = p2.ss;
        unq.erase(ans[0]);
    }
    else if(unq.count(p2.ss)){
        unq.erase(p2.ss);
        ans[0] = *unq.begin();
        ans[1] = p2.ss;
        ans[2] = p2.ff;
        unq.erase(ans[0]);
    }
    
    st.erase(ans[0]);
    st.erase(ans[1]);
    st.erase(ans[2]);
    pair<int,int> p3 = mp[qrt[2]];
    if(st.count(p3.ff)){
        ans[3] = p3.ff;
        st.erase(p3.ff);
    }
    else{
        ans[3] = p3.ss;
        st.erase(p3.ss);
    }
    pair<int,int> p4 = mp[qrt[3]];
    if(st.count(p4.ff)){
        ans[4] = p4.ff;
        st.erase(p4.ff);
    }
    else{
        ans[4] = p4.ss;
        st.erase(p4.ss);
    }
    ans[5] = *st.begin();
    printf("! %d %d %d %d %d %d", ans[0], ans[1], ans[2], ans[3], ans[4], ans[5]);
    cout << endl;
}

int main(){
//   Motto_Hayakku;
  ll test=1;
//   cin >> test;
//   ll cases = test;
  while(test--){
      solve();
  }
  return 0;
}