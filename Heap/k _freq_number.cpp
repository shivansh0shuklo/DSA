#include <iostream>
#include <utility>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

typedef pair<int,int> ppi;
priority_queue<ppi,vector<ppi>,greater<ppi>> minh;
unordered_map<int,int> mp;
#define fo(i,n) for(int i =0 ; i<n ; i++)

vector<int> k_frequent_number(vector<int> arr,int k){
    priority_queue<ppi,vector<ppi>,greater<ppi>> minh;
    unordered_map<int,int> mp;
    int n = arr.size();
    fo(i,n){
        mp[arr[i]]++;
    }
    //this is like the [arr[i],freq] --> map
    //now the heap wil be [freq,arr[i]] --> min heap
    for(auto j = mp.begin();j != mp.end();j++){
        minh.push({j->second,j->first});
        if(minh.size()>k){
            minh.pop();
        }

    }
    vector<int> vec;
    while(minh.size()>0){
        vec.push_back(minh.top().second);
        minh.pop();

    }
    return vec;

}

int main(){
    int k = 2;
    vector<int> arr = {1,1,1,2,2,3,4};
    vector<int> result = k_frequent_number(arr,k);
    cout << "[ "; 
    while(!result.empty()){
        cout << result.back() << " ";
        result.pop_back();
    }
    cout << "]";
}
