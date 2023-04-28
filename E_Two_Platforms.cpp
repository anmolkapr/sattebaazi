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
ll x[n],y[n];
ll k;
cin >> k;
map<ll,ll> mp;
for(i =0 ; i < n;i++){cin >> x[i];mp[x[i]]++;}
for(i =0 ; i < n;i++){cin >> y[i];}

vector<ll> val;
n = mp.size();
vector<ll> prsum ;
prsum.push_back(0);
for(auto i : mp){
    val.push_back(i.first);
    prsum.push_back(prsum.back() + i.second);
}

for(i =0 ; i <= n;i++){
    cout << prsum[i] << ' ';
}
cout << endl;
for(i =0 ; i < n;i++){
    cout << val[i] << ' ';
}

ll mxpts = 0;
ll in = 0 ;
ll ct =0 ;
for(i = k ; i < n;i++){
  if(mxpts < prsum[i+1] - prsum[i - k]){
    mxpts = prsum[i + 1] - prsum[i-k];
    in = i;
  }
}

for(i = k ; i < n;i++){
   if(prsum[i + 1] - prsum[i-k] == mxpts){
    ct++;
   }
}
cout << endl;
cout << ct << ' ' << val[in] << ' ' << mxpts << endl;





    
}
 
 ll x = 1;
int main(){
ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
int t=1;
//cin>>t;
while(t--){
x++;
  solve();
 cout << endl;
}
 
}


 