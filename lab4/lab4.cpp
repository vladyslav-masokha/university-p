#include <iostream>
#include <windows.h>
using namespace std;

struct Node {
  int data;
  Node* next;
};

Node* header = nullptr;

void append(int value) {
  Node* newNode = new Node{ value, nullptr };

  if (header == nullptr) {
    header = newNode;
  }
  else {
    Node* currentEl = header;

    while (currentEl->next != nullptr) {
      currentEl = currentEl->next;
    }

    currentEl->next = newNode;
  }
}

int search(int pos) {
  Node* currentEl = header;

  for (int i = 1; i < pos && currentEl != nullptr; i++)
    currentEl = currentEl->next;

  if (currentEl != nullptr) {
    return currentEl->data;
  }
  else {
    cout << "Неправильна позиція!" << endl;
    return -1;
  }
}

void remove(int pos) {
  if (pos == 1) {
    Node* tempEl = header;
    header = header->next;
    delete tempEl;
  }
  else {
    Node* currentEl = header;
    for (int i = 1; i < pos - 1 && currentEl != nullptr; i++) {
      currentEl = currentEl->next;
    }

    if (currentEl != nullptr && currentEl->next != nullptr) {
      Node* tempEl = currentEl->next;
      currentEl->next = tempEl->next;
      delete tempEl;
    }
    else {
      cout << "Неправильна позиція!" << endl;
    }
  }
}

void clear() {
  Node* currentEl = header;

  while (currentEl != nullptr) {
    Node* tempEl = currentEl;
    currentEl = currentEl->next;
    delete tempEl;
  }

  header = nullptr;
}

void display() {
  Node* currectEl = header;

  while (currectEl != nullptr) {
    cout << currectEl->data << " ";
    currectEl = currectEl->next;
  }
  cout << endl;
}

int main() {
  SetConsoleCP(1251);
  SetConsoleOutputCP(1251);

  append(6);
  append(62);

  cout << "Елементи списку: ";
  display();
  cout << search(2);
  clear();

  append(16);
  remove(1);
  display();

  append(165);
  display();
}
