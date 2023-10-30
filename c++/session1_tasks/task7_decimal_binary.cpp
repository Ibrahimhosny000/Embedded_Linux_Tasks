// ---------------------------------------------------------------------
//         change from decimal to binary and vice versa :-
// ---------------------------------------------------------------------

#include <iostream>
#include <bitset>
#include <string>
int main(){
    std::cout << "Choose '1' to convert from decimal to binary\nChoose '2' to convert from binary to decimal" << std::endl;
    int choice;
    std::cin>> choice;
    if(choice == 1){
        unsigned int decimal;
        std::cout << "Enter the number in decimal" << std::endl;
        std::cin>>decimal;
        std::string binary = std::bitset<8>(decimal).to_string();
        std::cout << binary << std::endl;
    }
    else if(choice == 2){
        std::cout << "Enter the number in binary" << std::endl;
        std::string binary ;
        std::cin >> binary ;
        std::bitset<8>bits(binary);
        unsigned long decimal = bits.to_ulong();
        std::cout << decimal << std::endl;
    }
    else
    {
        std::cout << "unrecognized choice" << std::endl;
    }

return 0;    
}
