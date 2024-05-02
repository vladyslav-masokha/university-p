#include <iostream>
#define SIZE 50
#define TOP -1

using namespace std;

int top = TOP;
int arr[SIZE];

// check stack
bool isEmpty() {
  return top == TOP;
}

// check stack
bool isFull() {
  return top == SIZE - 1;
}

// add element in stack
void push(int value) {
  if (isFull()) {
    cout << "Stack is full" << endl;
    return;
  }

  arr[++top] = value;
}

// delete element in stack
int pop() {
  if (isEmpty()) {
    cout << "Stack is empty" << endl;
    return -1;
  }

  return arr[top--];
}

// search top element in stack
int peek() {
  if (isEmpty()) {
    cout << "Stack is empty" << endl;
    return -1;
  }

  return arr[top];
}

// output stack
void display() {
  if (isEmpty()) {
    cout << "Stack is empty" << endl;
    return;
  }

  cout << "Stack: ";
  for (int i = top; i >= 0; i--) {
    cout << arr[i] << " ";
  }

  cout << endl;
}

int main() {
  int arr[SIZE];
  display();

  push(10);
  push(20);
  push(30);
  push(40);

  display();

  int value = pop();
  cout << "Popped value: " << value << endl;

  value = peek();
  cout << "Top value: " << value << endl;

  display();

  return 0;
}