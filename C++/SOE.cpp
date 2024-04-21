#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
Time Complexity

outer loop -> iterates from 0 to sqrt(n) which makes O(sqrt(n))
The number of iterations of the inner loop for each prime number p is approximately n/p (for 2 -> 100/2, for 3 -> 100/3)
​This sum is approximately n times the sum of the reciprocals of prime numbers up to n
According to the Prime Number Theorem, this sum is approximately log(log(n)).
*/

vector<int> sieveOfEratosthenes(int n){
    vector<int> result;
    vector<bool> isPrime(n+1, true);

    for(int p = 2; p * p <= n; p++){
        if(isPrime[p] == true){
            for(int i = p * p; i <= n; i += p){
                isPrime[i] = false;
            }
        }
    }

    for(int i = 2; i <= n; i++){
        if(isPrime[i]){
            cout << i << " ";
            result.push_back(i);
        }
    }

    return result;
}

int main(){
    int n = 100;
    cout << "prime number up to " << n << " are: ";
    sieveOfEratosthenes(n);
    return 0;

}