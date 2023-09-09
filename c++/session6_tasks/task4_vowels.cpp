// -------------------------------------------------------------------------
//              Decide if a letter is vowel or not :-
// -------------------------------------------------------------------------

#include <iostream>
#include <cctype>
char letter;
int main(){
    std::cout << "Enter a letter to see if it is vowel or NOT" << std::endl;
    std::cin>> letter;
if ( isalpha(letter)) { //is alpha chicks if user entered a letter or not
    if(letter == 'A' || letter == 'E' || letter == 'I' || letter == 'O' || letter == 'U'){
    std::cout << "The entered letter " << letter << " is a vowel" << std::endl;
    }
    else if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u') {
        std::cout << "The enterd letter " << letter << " is a vowel" << std::endl;
    }
    else
    {
     std::cout << "letter " << letter << " is 'NOT' a vowel" <<std::endl;
    }
}
else //if user entered any thing other than a letter
{
    std::cout << letter <<  " is not a letter" << std::endl;
}
    
return 0;
}