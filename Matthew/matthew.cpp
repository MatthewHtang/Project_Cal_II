#include <iostream>
#include <string>
#include <cmath>
using namespace std;

//Function to Differentiate u

string differentiate(string u)
{
    if (u == "x") return "1";
    if (u == "x^2") return "2x";
    if (u == "x^3") return "3x";
    
}

int main()
{
    string u, dv;

    cout << "Integration by Parts Solver" << endl;
    cout << "Formula : ∫u dv = u*v - ∫v du" << endl;

    cout << "Enter u: ";
    cin >> u;

    cout << "Enter dv: ";
    cin >> dv;

    //handeling simple case//

    if (u == "x" && dv == "e^x");
}
