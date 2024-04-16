#include <iostream>
#include <string>
using namespace std;

// Task 1
class Student {
    private:
        string name;
        string surname;
        int age;
        int ratingIdentifier;
   
    public:
        Student(string _name, string _surname, int _age, int _ratingIdentifier) {
            name = _name;
            surname = _surname;
            age = _age;
            ratingIdentifier = _ratingIdentifier;
        }

    // Destructor
    ~Student() {
        cout << "destructor finished" << endl;
    }

    string getName() { return name; }
    string getSurname() { return surname; }
    int getAge() { return age; }
    int getRatingIdentifier() { return ratingIdentifier; }

    void printInfo() {
        cout << "Name: " << name << endl;
        cout << "Surname: " << surname << endl;
        cout << "Age: " << age << endl;
        cout << "Rating Identifier: " << ratingIdentifier << endl;
    }

    void changeRating(int newRating) {
        ratingIdentifier = newRating;
    }
};

// Task 2
float inverse(float num) {
    return 1.0 / num;
}

int inverse(int num) {
    return 1 / num;
}

long inverse(long num) {
    return 1 / num;
}

// Task 3
template<typename T>
T inverse(T num) {
    return 1 / num;
}

int main() {
   
    Student student1("Saba", "Giorkhelidze", 20, 3);

    cout << "\nStudent1 Details:" << endl;
    student1.printInfo();

    student1.changeRating(2);

    cout << "\nchanged rating:" << endl;
    student1.printInfo();

    //Func overloading
    cout << "\nInverse float: " << inverse(2.5) << endl;
    cout << "Inverse int: " << inverse(5) << endl;
    cout << "Inverse Long: " << inverse(10L) << endl;

    //Template for func overloading
    cout << "\n inverse func template:" << endl;
    cout << "Inverse 3.5: " << inverse<float>(3.5) << endl;
    cout << "Inverse 7: " << inverse<int>(7) << endl;
    cout << "Inverse 15L: " << inverse<long>(15L) << endl;

    return 0;
}