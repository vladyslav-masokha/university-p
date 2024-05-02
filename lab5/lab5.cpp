#include <iostream>
#define SIZE 10
using namespace std;

int arr[2][SIZE];

int hashFunction(int key) {
  return key % SIZE;
}

int resolveCollision(int hash, bool insertMode, int key) {
  int start = hash;
  int probe = 0;
  bool found = false;

  while (!found) {
    if (insertMode) {
      if (arr[0][hash] == -1) found = true;
      else {
        probe++;
        hash = (start + probe) % SIZE;
      }
    }
    else {
      if (arr[0][hash] == key) found = true;
      else {
        probe++;
        hash = (start + probe) % SIZE;
      }
    }
  }

  return hash;
}

int insert(int key, int value) {
  int hash = hashFunction(key);
  int index = resolveCollision(hash, true, key);

  arr[0][index] = key;
  arr[1][index] = value;

  return index;
}

int remove(int value) {
  int indicesToRemove[SIZE];
  int numIndices = 0;
  int removedKeys[SIZE];
  int numRemovedKeys = 0;

  for (int i = 0; i < SIZE; i++) removedKeys[i] = -1;

  for (int i = 0; i < SIZE; i++) {
    if (arr[1][i] == value) {
      indicesToRemove[numIndices++] = i;
      removedKeys[numRemovedKeys++] = arr[0][i];
    }
  }

  if (numIndices == 0) {
    cout << endl;
    cout << "No elements found with value " << value << endl;
    return -1;
  }

  for (int i = 0; i < numIndices; i++) {
    int index = indicesToRemove[i];

    arr[0][index] = -1;
    arr[1][index] = -1;
  }

  for (int i = 0; i < SIZE; i++) {
    if (arr[0][i] != -1) {
      int newIndex = resolveCollision(hashFunction(arr[0][i]), true, arr[0][i]);

      arr[0][newIndex] = arr[0][i];
      arr[1][newIndex] = arr[1][i];
      arr[0][i] = -1;
      arr[1][i] = -1;
    }
  }

  cout << "Removed keys with value " << value << ": ";
  for (int i = 0; i < numRemovedKeys; i++) {
    if (removedKeys[i] != -1) cout << removedKeys[i] << " ";
  }
  cout << endl;

  return (numRemovedKeys > 0) ? removedKeys[0] : -1;
}

int getValue(int key) {
  int hash = hashFunction(key);
  int index = resolveCollision(hash, false, key);

  return arr[1][index];
}

void display() {
  cout << "Key\tValue" << endl;
  for (int i = 0; i < SIZE; i++) {
    if (arr[0][i] != -1) cout << arr[0][i] << "\t" << arr[1][i] << endl;
  }
}

int main() {
  for (int i = 0; i < SIZE; i++) {
    arr[0][i] = -1;
    arr[1][i] = -1;
  }

  insert(123, 10);
  insert(456, 20);
  insert(789, 10);
  insert(321, 30);
  insert(654, 10);

  cout << "Initial table:" << endl;
  display();

  remove(14);
  cout << "\nAfter removing values 10:" << endl;
  display();

  cout << "\nValue of key 456: " << getValue(456) << endl;

  return 0;
}