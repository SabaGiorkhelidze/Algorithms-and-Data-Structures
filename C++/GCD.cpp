#include <iostream>
using namespace std;

int gcd(int a, int b){
    if(a==0){
        return b;
    }
    return gcd(b % a, a);
    
}

int main(){
    int a = 240, b = 60;

    cout << gcd(a, b) << endl;
    return 0;
}

