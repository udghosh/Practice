#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int n;
    int i=0;
    cin >> n;

    //write your code here
    int x=0;
    int count=0;
    while(n){
       x = (n%10)-1;
       count++;
       i = i + (pow(10,x)*count);
       n = n/10;
    }
    cout<<i<<endl;
}