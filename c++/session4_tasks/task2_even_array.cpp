// ---------------------------------------------------------------
//              -check if all the array is even ?
// ---------------------------------------------------------------

#include <iostream>

int main() {
  
  int arr[] = {2, 4, 6, 8, 10,12,14,16};
  int size = sizeof(arr) / sizeof(arr[0]);

  bool checker = true;
  for (int i = 0; i < size; i++) {
    if (arr[i] % 2 != 0) {
      checker = false;
      std::cout << "Not all the elements is the array are even" << std::endl;
      break;
    }
  }
  
  if (checker) {
    std::cout << "The elements in the array are even" << std::endl;
  }

  return 0;
}