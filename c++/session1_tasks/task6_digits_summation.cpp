// ---------------------------------------------------------------
//       summation the digits of integer entered by user:-
// ---------------------------------------------------------------

#include <iostream>

using namespace std;
int main() {
  int num, lastnum;
  int sum = 0;

  cout << "Enter a number to be added : ";
  cin >> num;
  while (num) {
    lastnum = num % 10;  // % 10 extracts the last number
    sum += lastnum;      // add this number to the sum which is initialy equals 0
    num /= 10;           // divide the num by 10 to take out last num that was added to sum
  }
  cout << "The sum of the number is => " << sum << endl;

  return 0;
}