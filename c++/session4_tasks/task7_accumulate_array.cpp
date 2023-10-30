// ---------------------------------------------------------------
//                -calculate accumulate of array
// ---------------------------------------------------------------

#include <iostream>
#include <numeric>

int main() {

  int arr[] = {1, 2, 3, 4, 5,6,7,8,9};

  int accumulate = std::accumulate(std::begin(arr), std::end(arr),0);  // 0 value is the value added to the accumulation of the array 

  std::cout << "The accumulate of the array is: " << accumulate << std::endl;

  return 0;
}
