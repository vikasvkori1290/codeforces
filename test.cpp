#include <iostream>
using namespace std;

int main() {
    int n = 30;

    if (n % 3 == 0)
        cout << "A";
    else if (n % 5 == 0)
        cout << "B";
    else if (n % 15 == 0)
        cout << "C";
    else
        cout << "D";

    return 0;
}