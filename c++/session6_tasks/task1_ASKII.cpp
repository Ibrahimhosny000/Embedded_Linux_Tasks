// -------------------------------------------------------------------
//               create a table for ASKII code :-
// -------------------------------------------------------------------

#include <iomanip>
#include <iostream>
int main(){
    std::cout<<"ASCII code table:"<<std::endl;
    std::cout<<"+-------+-------+"<<std::endl;
    std::cout<<"| Char  | ASCII |"<<std::endl;
    std::cout<<"+-------+-------+" << std::endl;
    unsigned int i;
    for(i = 32; i <=126; ++i )
    std::cout <<"|"<<std::setw(4)<< char(i)<<std::setw(9) <<i <<"  |"<<std::endl;

return 0;
}