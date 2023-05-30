#include <iostream>
using namespace 

void pattern1() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 1; j <= n; j++) {
      cout << j << " ";
    }
    cout << endl;
  }
}

void pattern2() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 1; j <= n; j++) {
      cout << n - j + 1 << " ";
    }
    cout << endl;
  }
}

void pattern3() {
  int n, count = 1;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 1; j <= n; j++) {
      cout << count << " ";
      count++;
    }
    cout << endl;
  }
}

void pattern4() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++)
      cout << "*";
    cout << endl;
  }
}

void pattern5() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
      cout << i;
    }
    cout << endl;
  }
}

void pattern6() {
  int n, count;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    count = i;
    for (int j = 1; j <= i; j++) {
      cout << count << " ";
      count++;
    }
    cout << endl;
  }
}

void pattern7() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
      cout << i - j + 1 << ' ';
    }
    cout << endl;
  }
}

void pattern8() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = n - i; j >= 0; j--) {
      cout << "  ";
    }
    for (int k = 1; k <= i; k++) {
      cout << k << " ";
    }
    for (int l = i - 1; l >= 1; l--) {
      cout << l << " ";
    }
    cout << endl;
  }
}

void pattern9() {
  // Make this final pattern...
  // 1234554321
  // 1234**4321
  // 123****321
  // 12******21
  // 1********1
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int i = 1; i <= n; i++) {
    }
    cout << endl;
  }
}

void pattern() {
  pattern1();
  pattern2();
  pattern3();
  pattern4();
  pattern5();
  pattern6();
  pattern7();
  pattern8();
  pattern9();
}

int binarySearch(int arr[] , int size , int key){
    int start = 0;
    int end = size-1;
    int mid = (start + end)/2;
    while ( start <= end){
        if(arr[mid] == key){
            return mid;
        }
        // Go to right wala
        if (key > arr[mid]){
            end = mid - 1;
        }
        else{
            end = mid +1;
        }
        mid = {(start + end)/2};
    }
    return -1;
} 


int main() { 
    // pattern();
    int even[6] = {2,4,6,8,12,18};
    int size = 6;
    int key = 2;
    int index =binarySearch(even , size , key);
    cout<<"Index of "<<key<<" is : "<<index;
}