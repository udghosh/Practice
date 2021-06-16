#include <iostream>
#include<cmath>

using namespace std;
int main(){
    int n,k;
    cin>>n>>k;
    
    //write your code here
    int m = n;
    int count = 0;
    int val = 0;
    int x = 0;
    
    while(m){
        count++;
        m = m/10;
    }
    
    
    if(k<0){
        k=abs(k);
         k = k%count;
        k = count - k;
    }

    if(k>0){
        k = k%count;
    }
    while(k){
        x = n%10;
        val = val + (pow(10,(count-k))*x);
        n = n/10;
        k--;
    }
    val = val + n;
    cout<<val<<endl;
}