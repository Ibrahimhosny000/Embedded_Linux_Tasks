// ---------------------------------------------------------------
//             maximum number between three valuse :-
// ---------------------------------------------------------------

#include <iostream>
int x, y, z;
int main(){
    std::cout << "Enter three numbers to\ndetermine which is maximum" << std::endl;
    std::cin>> x >> y >> z;
    if(x >= y && x >= z){
        std::cout << "Max number is " << x <<std::endl;
    }
    else if( y >= x && y >= z){
        std::cout << "Max number is " << y << std::endl;
    }
    else {
    std::cout << "Max number is " << z << std::endl;
    }

return 0;
}