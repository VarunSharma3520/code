/*https://www.w3schools.com/cpp/*/
#include <iostream>

using namespace std;


namespace customNameSpace {

  int x = 10;
  int y = 20;
  int add(int a, int b) {
    return a + b;
  }
}
int main () {
  // x can't be changed
  const int x = 10;
  cout << customNameSpace::add(customNameSpace::x, customNameSpace::y) << endl;
  cout << "Hello, World!\n"; 

  return 0;
} 
