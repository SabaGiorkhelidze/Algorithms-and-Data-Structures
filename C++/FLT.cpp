#include <iostream>

// Function to compute (base^exponent) % modulus efficiently using modular exponentiation
// Parameters:
//   base (int): The base.
//   exponent (int): The exponent.
//   modulus (int): The modulus.
// Returns:
//   int: The result of (base^exponent) % modulus.
int powerMod(int base, int exponent, int modulus) {
    int result = 1;
    base = base % modulus;  
    while (exponent > 0) {
        if (exponent % 2 == 1) {  
            result = (result * base) % modulus;  
        }
        exponent /= 2;  
        base = (base * base) % modulus;  
    }
    return result;
}

// Function to check if 'a' satisfies Fermat's Little Theorem modulo prime 'p'
// Parameters:
//   a (int): The integer to be tested.
//   p (int): The prime number.
// Returns:
//   bool: True if 'a' satisfies Fermat's Little Theorem modulo 'p', False otherwise.
bool fermatLittleTheorem(int a, int p) {
    if (powerMod(a, p - 1, p) == 1) {  
        return true;  
    }
    return false;  
}

int main() {
    int a = 2;  
    int p = 5;
    if (fermatLittleTheorem(a, p)) {  
        std::cout << a << " satisfies Fermat's Little Theorem modulo " << p << std::endl;
    } else {
        std::cout << a << " does not satisfy Fermat's Little Theorem modulo " << p << std::endl;
    }
    return 0;  
}
