#include <utility>
#include <queue>
#include <iostream>
#include <cmath>
#include <vector>
 
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;
typedef pair<int,int> ppi;
using maxheap = priority_queue<ppi>;


maxheap kclosest(vector<int> arr,int k,int x){
    maxheap maxh;
    f(i,arr.size()){
        maxh.push({abs(x-arr[i]),arr[i]});
        if(maxh.size()>k){
            maxh.pop();
        }

    }    
    return maxh;
}

int main(){
    vector<int> arr = {5,6,7,8,9};
    int x = 7;
    int k = 3;
    maxheap vec = kclosest(arr,k,x);
    vector<int> result;
    int i = 0;
    while(i<k){
        i++;
        ppi topele = vec.top();
        result.push_back(topele.second);
        vec.pop();
    }
    while(!result.empty()){
        cout << result.back() << " ";
        result.pop_back();
    }

}
