// -------------------------------------------------------------------------------------
//           Write a lambda function to calculate the square of a given number :- 
// -------------------------------------------------------------------------------------

#include <iostream>

int main(){

    auto fn = [](int x){
        std::cout << "square of '"<< x << "' is --> " << x * x << std::endl;
        };

    std::cout << "Enter a number to see its square ";
    int num;
    std::cin>> num;
    fn(num);
    
return 0;
}
