// ---------------------------------------------------------------
//              -check if the character is digit ?
// ---------------------------------------------------------------

#include <iostream>
#include <cctype>

void check(char x){
    
    if(std::isdigit(x)){
        std::cout << x  << " is a digit" << std::endl;
    }
    else {
        std::cout << x  << " is NOT a digit" << std::endl;
    }
}

int main(){
    char I;
    std::cout << "Enter a character to see if it's a digit or not" << std::endl;
    std::cin>> I;
    check(I);
return 0;
}
