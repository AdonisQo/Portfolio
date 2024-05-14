#include <iostream>
#include <regex>
using namespace std;

int main(){

int strength = 0;
cout << "Enter Password: ";
string pass;
cin >> pass;

if (regex_search(pass, regex("[A-Z]+")))
    strength +=20;
if (regex_search(pass, regex([a-z]+)))
strength +=20;
if (regex_search(pass, regex([0-9]+)))
strength +=20;
if (regex_search(pass, regex([`~!@#$%^&*-_=+]+)))
strength +=20;
if (pass.length() >= 8)
strength +=20

if (strength == 100)
cout << " Your password is very secure";
else if(strength == 80)
cout << "Your password is secure";
else if(strength == 60)
cout << "Your password is moderately secure";
else if(strength == 40)
cout << "Your password is remotely secure";
else if(strength == 20)
cout << "Your password is weak";
else (strength == 0)
cout << "Your password is very weak";
return 0;
}
