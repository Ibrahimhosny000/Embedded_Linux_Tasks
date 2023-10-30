// ---------------------------------------------------------------
//          -fill array from 10 to 10000 sequentially
// ---------------------------------------------------------------


#include <iostream>
#include <numeric>  

int main() 
{
    int size = 9991;  // from 10 to 10000  
    int arr[size];         

    std::iota(arr, arr + size, 10);    // 10 is the intial value

    for (int i = 0; i < 5; ++i)    // for loop to display the wanted values
    {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

return 0;
}



