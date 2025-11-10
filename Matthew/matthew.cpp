#include <iostream>
#include <string>
using namespace std;

string findDerivative(string u)
{
    int coef = 1;   
    int powr = 1;   

    //handling ln(x) & trig functions
    if (u == "ln(x)")
        return "1/x";
    
    // find coefficient before 'x'
    string num = "";
    for (int i = 0; i < u.size(); i++)
    {
        if (u[i] == 'x')
            break; // stop once we hit x
        num += u[i];
    }

    // if we found a number before x, update coef
    if (num != "")
        coef = stoi(num);

    // find power if '^' exists
    for (int i = 0; i < u.size(); i++)
    {
        if (u[i] == '^')
        {
            string p = "";
            for (int j = i + 1; j < u.size(); j++)
            {
                p += u[j];
            }
            powr = stoi(p);
        }
    }


    int newCoef = coef * powr;
    int newPow = powr - 1;


    string result = to_string(newCoef);
    if (newPow == 0)
        return result; 
    else if (newPow == 1)
        result += "x";
    else
        result += "x^" + to_string(newPow);

    return result;

}

string findIntegral(string dv)
{
    // basic trig and exponential
    if (dv == "sin(x)")
        return "-cos(x)";
    if (dv == "cos(x)")
        return "sin(x)";
    if (dv == "e^x")
        return "e^x";
    if (dv == "e^-x")
        return "-e^-x";
    if (dv == "1")
        return "x";

    // handle sin(3x) or cos(3x)
    if (dv.find("sin(") != string::npos)
    {
        int coef = dv[dv.find("(") + 1] - '0'; // get number after '('
        string result = "-(1/" + to_string(coef) + ")cos(" + to_string(coef) + "x)";
        return result;
    }

    if (dv.find("cos(") != string::npos)
    {
        int coef = dv[dv.find("(") + 1] - '0'; // get number after '('
        string result = "(1/" + to_string(coef) + ")sin(" + to_string(coef) + "x)";
        return result;
    }

    // handle e^3x or e^-3x
    if (dv.find("e^") != string::npos)
    {
        int pos = dv.find("^");
        int sign = 1;
        int coef = 1;

        if (dv[pos + 1] == '-')  // e^-3x
        {
            sign = -1;
            coef = dv[pos + 2] - '0';
        }
        else                     // e^3x
        {
            coef = dv[pos + 1] - '0';
        }

        string frac = "(1/" + to_string(coef) + ")";
        if (sign == -1)
            return "-"+frac+"e^-"+to_string(coef)+"x";
        else
            return frac+"e^"+to_string(coef)+"x";
    }

    return "unknown";


}
string findSecondIntegral(string v, string du)
{
    string term = v + "*" + du;

    // Handle common simple cases manually
    if (v == "sin(x)" && du == "1")
        return "-cos(x)";
    if (v == "-cos(x)" && du == "1")
        return "-sin(x)";
    if (v == "cos(x)" && du == "1")
        return "sin(x)";
    if (v == "e^x" && du == "1")
        return "e^x";

    // fallback
    return "∫(" + term + ")dx";
}


int main()
{
    string u, dv, du, v;

    cout << "Enter u (like x^2 or 3x^2): ";
    cin >> u;
    cout << "Enter dv (like cos(x), sin(3x), e^x): ";
    cin >> dv;

    du = findDerivative(u);
    v = findIntegral(dv);
    string secondPart = findSecondIntegral(v, du);

    // ∫u dv = uv - ∫v du
    string finalAnswer = "(" + u + ")*(" + v + ") - (" + secondPart + ") + C";

    cout << "\n---- Results ----\n";
    cout << "u  = " << u << endl;
    cout << "du = " << du << endl;
    cout << "v  = " << v << endl;
    cout << "\nFinal Answer: " << finalAnswer << endl;

    return 0;
}