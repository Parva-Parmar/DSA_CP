/*
https://codeforces.com/problemset/problem/1143/C
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

bool sortbysec(const pair<int,int> &a,const pair<int,int> &b)
{
    return (a.ss < b.ss);
}

ll modd = 998244353;
const int NMAX = 2e5+5;
vector<pair<ll,ll>> g[NMAX];

void dfs(vector<vector<ll>> &g , vector<ll> &vis , vector<ll> &c , ll parent , vector<ll> &del){
    for(auto i : g[parent]){
        if(c[i] == 0){
            // cout << "parent " << parent << " " << " i " << i << nl;
            del[parent] = 0;
        }
    }
    for(auto i : g[parent]){
        if(vis[i] == 0){
            vis[i] = 1;
            dfs(g,vis,c,i,del);
        }
    }
}

void solve(){
    ll n;
    cin >> n;
    vi c(n+1);
    vector<vector<ll>> g(n+1);
    vi vis(n+1);
    ll root = 0;
    for(int i = 0 ; i < n ; i++){
        ll x,y;
        cin >> x >> y;
        
        // cout << x << " " << y << nl;
        if(x != -1){
            g[x].pb((i+1));
        }
        else{
            root = (i+1);
        }
        
        c[i+1] = y;
    }
    vi del(n+1 , 1);
    vis[root] = 1;
    dfs(g,vis,c,root,del);
    
    vi ans;
    
    for(int i = 1 ; i <=n ; i++){
        if(i != root){
            if(c[i] == 1 && del[i] == 1){
                ans.pb(i);
            }
        }
    }
    if(ans.size() == 0){
        cout << -1 << nl;
        return;
    }
    // cout << "del" << nl;
    // cout(del);
    // cout << "c" << nl;
    // cout(c);
    // cout << "ans" << nl;
    cout(ans);
}

int main(){
  Motto_Hayakku;
  ll test=1;
//   cin >> test;
  ll cases = test;
  while(test--){
    solve();
  }
  return 0;
}