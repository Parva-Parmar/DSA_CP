/*
https://codeforces.com/problemset/problem/1692/G
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
 
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;

template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

 

/*
 
1. Think Greedy
2. Think Brute Force
3. Think solution in reverse order
4. Think DP [ check constraints carefully ]
5. Check base cases for DP and prove solution for Greedy
6. Think Graph 
 
*/

bool srt(const pair<ll,ll> &a, const pair<ll,ll> &b){
    if(a.ff!= b.ff){
        return a.ff < b.ff;
    }
    else{
        return b.ss > a.ss;
    }
}

set<ll> printDivisors(ll n){set<ll> v;for (ll i=1; i<=sqrt(n); i++){if (n%i == 0){if (n/i == i)v.insert(i);else{v.insert(i);v.insert(n/i);}}}return v;}
 
class Disjointset {
    vector<ll> size,parent;
public:
    Disjointset(int n){
        size.resize((n+1),1);
        parent.resize(n+1);
        iota(parent.begin(),parent.end(),0);
    }
 
    int findUpar(int node){
        if(node == parent[node]){
            return node;
        }
        return findUpar(parent[node]);
    }
 
    void unionBySize(int u , int v){
        int ulp_u = findUpar(u);
        int ulp_v = findUpar(v);
        if(ulp_v == ulp_u){
            return;
        }
        if(size[ulp_u]<size[ulp_v]){
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }
        else{
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
};

bool sortbysec(const pair<ll, pair<ll,char>> &a, const pair<ll, pair<ll,char>> &b)
{
    if(a.ff != b.ff){
        return a.ff < b.ff;
    }
    else{
        return a.ss.ff > b.ss.ff;
    }
}

ll modd = 998244353;
const int NMAX = 2e5+5;
vector<pair<ll,ll>> g[NMAX];

void dfs(vector<ll> &dp,vector<ll> &id,ll parent){
    for(auto it : g[parent]){
        if(dp[it.ff] == 0){
            dp[it.ff] = dp[parent] + (it.ss <= id[parent]);
            id[it.ff] = it.ss;
            dfs(dp,id,it.ff);
        }
    }
}

void solve(){
    ll n,k;
    cin >> n >> k;
    vi a(n);
    in(a);
    ll cnt = 1;
    ll ans = 0;
    for(ll i = 0 ; i < n-1 ; i++){
        if(a[i] < 2*a[i+1]){
            cnt++;
        }
        else{
            cnt = 1;
        }
        
        if(cnt > k){
            ans++;
        }
    }
    cout << ans << nl;
}

int main(){
  Motto_Hayakku;
  ll test=1;
  cin >> test;
  ll cases = test;
  while(test--){
    solve();
  }
  return 0;
}