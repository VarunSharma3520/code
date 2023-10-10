#include<iostream>

using namespace std;


int main(){
    int a = 3;
    int* b = &a;
    cout<<"Address of a : "<<&a<<endl;
    cout<<"Address of a : "<<b;
    return 0;
}