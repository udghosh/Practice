#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int temp; 
    int mul = 1;
    temp = n;
    while(temp >= 10){
        temp = temp/10;
        mul = mul*10;
        
    }
    cout<<mul<<endl;
    temp = n;
    while(temp){
        int num = temp/mul;
        cout<<num<<endl;
        temp = temp%mul;
        mul = mul/10;
    }
}