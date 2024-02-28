#include <iostream>
using namespace std;

int main() {
  double number1, number2;

  cout << "Enter number1: ";
  cin >> number1;

  cout << "Enter number2: ";
  cin >> number2;

  cout << "Sum: " << number1 + number2 << endl;
  cout << "Dif: " << number1 - number2 << endl;
  cout << "Mult: " << number1 * number2 << endl;

  if (number2 != 0) cout << "Div: " << number1 / number2 << endl;
  else cout << "Cannot divide by zero" << endl;

  if (number2 != 0) cout << "Remainder: " << fmod(number1, number2) << endl;
  else cout << "Cannot divide by zero" << endl;

  return 0;
}