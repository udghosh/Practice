#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    if(n==0){
        cout<<"Invalid"<<endl;
    }
    else{
    int a = 0;
    int b = 1;
    for(int i=0;i<n;i++){
        cout<<a<<endl;
        int c = a+b;
        a = b;
        b = c;

    }
    }
}