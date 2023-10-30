// ------------------------------------------------------------
//           Write a lambda functions to sort an array 
//           of integers in ascending and descending :- 
// ------------------------------------------------------------

#include <algorithm>
#include <iostream>

int main(){
    int arr[]={2,6,1,89,12,13,55,22,124,65};
    std::sort(std::begin(arr),std::end(arr),[](int a, int b){return a < b;});

    std::cout << "numbers in ascending order: " << std::endl;
     for(int i :arr){
        std::cout << i << " ";
     }
     std::cout << "\n---------------------------" <<std::endl;

    std::sort(std::begin(arr),std::end(arr),[](int a, int b){return a > b;});

        std::cout << "numbers in descending order: " << std::endl;
     for(int i :arr){
        std::cout << i << " ";
     }
     std::cout << std::endl;

return 0;
}
