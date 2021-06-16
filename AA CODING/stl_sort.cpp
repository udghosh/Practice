#include<bits/stdc++.h>
using namespace std;


int main(){
    vector <int> vec{1,8,9,4,1,3,45,56,2,12,34,0,98};
    sort(vec.begin(),vec.end(),greater<int>());
    for(int i:vec){
        cout<<i<<" ";
    }
    cout<<"\n";
    int arr[13] = {1,8,9,4,1,3,45,56,2,12,34,0,98};
    sort(arr,arr+6,greater<int>());
    for(int i:arr){
        cout<<i<<" ";
    }


}