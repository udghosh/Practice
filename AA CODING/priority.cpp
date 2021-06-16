# include<bits/stdc++.h>
using namespace std;

void print_queue(priority_queue<int,vector<int>,greater<int>> q){
    while(!q.empty()){
        cout<<q.top()<<endl;
        q.pop();
    }
}
int main(){
    priority_queue<int,vector<int>,greater<int>> q;
    for(int data : {1,8,7,5,6,6,7,3,4}){
        q.push(data);
    }
    print_queue(q);
}