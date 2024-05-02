#include <iostream>
#include <string>
using namespace std;

int main() {
  string str, modificatedStr;

  cout << "Enter your string: ";
  getline(cin, str);

  for (char l : str) {
    if (l != ' ') modificatedStr += l;
  }

  cout << modificatedStr << endl;
}
