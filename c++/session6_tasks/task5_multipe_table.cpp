// ----------------------------------------------
//           Multiplication table :-
// ----------------------------------------------

#include <iostream>
int main(){
    std::cout << "Enter a number to display it's\nmultiplication table " << std::endl;
    int num, x, mux;
    std::cin>> num;
    std::cout << "The multiplication table of " << num << " is:-" <<std::endl;
    for( x = 0; x <= num; ++x){
        mux = num * x;
        std::cout << num << "*" << x << " = "<< mux <<std::endl;
    }
return 0;
}