#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define ld long double  
ll i,n;
ll mod = 139 + 7;
ll find_nth_root(ll X, int n)
{ll nth_root=std::trunc(std::pow(X,1.0/n));if(std::pow(nth_root+1,n)<=X){return nth_root + 1;}
return nth_root;} 
bool checkperfectsquare(ll n){ if (ceil((double)sqrt(n)) == floor((double)sqrt(n)))
{ return true; }else{ return false; } }
ll bexp(ll a, ll b){ ll res = 1; while (b > 0) { if (b & 1) res = res * a; a = a * a; b >>= 1; } 
return res; }
ll bexpM(ll a, ll b, ll mod) { ll res = 1; while (b > 0) 
{ if (b & 1) res = (res * a) % mod; a = (a%mod * a%mod) % mod; b >>= 1; } return res; }
vector<ll> divisorsofanum(ll n){ vector<ll> v; for(i= 2; i < sqrt(n);i++){ if(n%i == 0)
{ v.push_back(i); v.push_back(n/i); } }
if(checkperfectsquare(n) == 1){ v.push_back(sqrt(n)); } return v; }
void precision(int a){ cout << setprecision(a) << fixed << endl; } 
ll modInverse(ll a, ll m){return bexpM(a,m - 2, m);}
ll gpsum(ll a, ll r, ll t){ll rpow = bexpM(r,t,mod);
ll ans = ((( rpow%mod + mod - 1)%mod)*(a%mod))%mod;
ans = ans%mod*(modInverse((r%mod - 1 + mod)%mod, mod)%mod);ans = ans%mod;return ans;}

const int P = 1e6;
bool prime[P + 1];

void SieveOfEratosthenes(int n)
{memset(prime, true, sizeof(prime));
for (int p = 2; p * p <= n; p++){if (prime[p] == true)
{for (int i = p * p; i <= n; i += p)prime[i] = false;}}}
vector<ll> adj[100010];bool visited[100010];vector<ll> graph;
void dfs(ll node){graph.push_back(node);visited[node]=true;
for(auto x: adj[node]){if(!visited[x]){dfs(x);}}}
 
 
 
 
 



 
 
 
void solve(){
    ll n;
    cin >> n;
    ll arr[n];
    for(i =0 ; i < n;i++){
        cin >> arr[i];

    }
    map<ll,ll> mp;
    for(i =0 ;i < n;i++){
        mp[arr[i]]++;
    }
    ll mex = 0;
    
    for(auto i : mp){
       if(i.first == mex){
        mex++;
       }
    }
    
    if(mp.count(mex + 1) == 0){
        if(mex == n){
            cout << "No";
        }else{
            cout << "Yes";
        }
    }else{
        
        ll l = INT_MAX,r = -1;
        for(i =0 ; i < n;i++){
           if(arr[i] == mex + 1){
            r = max(r,i);
            l = min(i,l);
           }
        }
      
        mp.clear();
        for(i = l ; i <= r; i++){arr[i] = mex;}
        ll mex1 = 0;
        for(i =0 ; i < n;i++)mp[arr[i]]++;
        for(auto i : mp){
           if(i.first == mex1){
            mex1++;
           }
        }
      
       if(mex1 == mex + 1){
        cout << "Yes";
       }else{
        cout << "No";
       }
        
    }



    
}
 
 ll x = 1;
int main(){
ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
int t=1;
cin>>t;
while(t--){
x++;
  solve();
 cout << endl;
}
 
}


 