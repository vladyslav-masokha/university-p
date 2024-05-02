#include <iostream>
using namespace std;

enum class Brand { APPLE, SAMSUNG, XIAOMI };
enum class Model { IPHONE, GALAXY, MI };

struct PhoneInfo {
  Brand brand;
  Model model;
  int year;
  double screenSize;
};

int main() {
  PhoneInfo phone;
  int brandValue, modelValue;

  cout << "Enter the brand of the phone (0 - Apple, 1 - Samsung, 2 - Xiaomi): ";
  cin >> brandValue;
  phone.brand = static_cast<Brand>(brandValue);

  cout << "Enter the model of the phone (0 - iPhone, 1 - Galaxy, 2 - MI): ";
  cin >> modelValue;
  phone.model = static_cast<Model>(modelValue);

  cout << "Enter the year of release: ";
  cin >> phone.year;

  cout << "Enter the screen size: ";
  cin >> phone.screenSize;

  cout << "Phone Brand: ";
  switch (phone.brand) {
  case Brand::APPLE:
    cout << "Apple";
    break;
  case Brand::SAMSUNG:
    cout << "Samsung";
    break;
  case Brand::XIAOMI:
    cout << "Xiaomi";
    break;
  }
  cout << endl;

  cout << "Phone Model: ";
  switch (phone.model) {
  case Model::IPHONE:
    cout << "iPhone";
    break;
  case Model::GALAXY:
    cout << "Galaxy";
    break;
  case Model::MI:
    cout << "MI";
    break;
  }
  cout << endl;

  cout << "Year of release: " << phone.year << endl;
  cout << "Screen size: " << phone.screenSize << " inches" << endl;
}
