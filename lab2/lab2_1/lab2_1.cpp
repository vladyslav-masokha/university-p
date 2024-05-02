#include <iostream>
#define SIZE 12
using namespace std;

int main() {
  double arr[SIZE];
  double* min, * max;
  int minIndex = 0, maxIndex = 0;

  for (size_t i = 0; i < SIZE; i++) {
    cout << "Enter num" << i + 1 << ": ";
    cin >> arr[i];
  }

  cout << "Array: ";
  for (size_t i = 0; i < SIZE - 1; i++) {
    cout << arr[i] << ", ";
  }
  cout << arr[SIZE - 1] << '.';
  cout << endl;

  min = max = &arr[0];

  for (size_t i = 0; i < SIZE; i++) {
    if (arr[i] < *min) {
      min = &arr[i];
      minIndex = i;
    }
  }

  for (size_t i = 0; i < SIZE; i++) {
    if (arr[i] > *max) {
      max = &arr[i];
      maxIndex = i;
    }
  }

  cout << "Min: " << *min << endl;
  cout << "Max: " << *max << endl;
  cout << "Counts elements between min & max elements: " << abs(maxIndex - minIndex) - 1 << endl;

  return 0;
}