#include<iostream>
using namespace std;

int print(int n){
        if(n==0 || n==1){
            
            return 0;
        
        }
        if(n==2){
             
            return 1;
           
        }
        if(true){
            return(print(n-1)+print(n-2));
            
        }
    }

int main(){
    int num;
    cin>>num;
    for(int i=1;i<=num;i++){
    cout<<print(i)<<endl;
    }
    return 0;
}