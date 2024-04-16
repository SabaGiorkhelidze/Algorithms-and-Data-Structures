#include <iostream>
#include <vector>
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

/*

int euclidean_algorithm(int a, int b) {

while (b != 0) {

int temp = b;

b = a % b;

a = temp;

}

return a;

}
*/