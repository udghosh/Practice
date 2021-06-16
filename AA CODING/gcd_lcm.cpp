#include <iostream>
using namespace std;
int main(int argc, char **argv){
    int num1, num2;
    int num =0;
    int x = 0;
    cin >> num1 >> num2;

    //write your code here
    if(num1>num2){
        num = num2; 
    }
    else{
       num = num1; 
    }
    for(int i=1; i<=num; i++){
        if(num1%i == 0 && num2%i == 0){
            x = i;
        }
    }
    cout<<x<<endl;  
    x = 0;
    num = 0;
    for(int i=1; ;i++){
        for(int j=1; ;j++){
            if(num1>num2){
                num = num2; 
                if(num1*i==num*j){
                    x = i;
                    if(num*j>num1*i){
                        break;
                    }
                    break;
                }
            }
            else{
                num = num1;
                if(num2*i==num*j){
                    x = i;
                    if(num*j>num2*i){
                        break;
                    }
                    break;
                }
            }
        }
    }
    cout<<num1*x<<endl;
}
