#include<iostream>
using namespace std;

int main(){
    double n;
    int m;
    int count=0;
    cin>>n;
    m = (int)n;
    cout<<m<<endl;
    while(m){
       m = m/10;
       count++;
           }
    cout<<count;
}