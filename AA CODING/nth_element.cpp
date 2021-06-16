#include<bits/stdc++.h>
using namespace std;


int main(){
    vector <int> vec{1,8,9,4,1,3,45,56,2,12,34,0,98};
    nth_element(vec.begin(),vec.begin()+1,vec.end(),greater<int>());
    
    cout<<"The Second Largest Element is : "<<vec[1]<<endl;

    nth_element(vec.begin(),vec.begin()+1,vec.end());
    
    cout<<"The Second smallest Element is : "<<vec[1]<<endl;
}