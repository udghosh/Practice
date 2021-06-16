#include<iostream>
using namespace std;
 int main(){
     int n;
     cin>>n;

     int nspace = 1;
     int nstar = n/2 + 1;

     for(int i=1;i<=n;i++){
         for(int j=1;j<=nstar;j++){
             cout<<"*\t";
         }
         for(int j=1;j<=nspace;j++){
             cout<<"\t";
         }
         for(int j=1;j<=nstar;j++){
             cout<<"*\t";
         }
         

         if(i<=n/2){
             nspace += 2;
             nstar --;
         }
         else{
             nspace -= 2;
             nstar ++;
         }
         cout<<endl;
         
     }
 }