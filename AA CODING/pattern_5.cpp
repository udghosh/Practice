#include<iostream>
using namespace std;
 int main(){
     int n;
     cin>>n;

     int nstar = 1;
     int nspace = n/2;

     for(int i=1;i<=n;i++){
         for(int j=1;j<=nspace;j++){
             cout<<"\t";
         }
         for(int j=1;j<=nstar;j++){
             cout<<"*\t";
         }
         if(i<=n/2){
             nspace --;
             nstar += 2;
         }
         else{
             nspace ++;
             nstar -= 2;
         }
         cout<<endl;
     }
 }