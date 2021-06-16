#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter A Number"<<endl;
    cin>>n;
    int num=2;
    while(num*num <= n){
        if(n%num==0){
            break;
        }
        num++;
    }
    if(num*num>n){
        cout<<"prime"<<endl;
    }
    else{
        cout<<"not prime"<<endl;
    }
    cout<<num<<endl;
}
