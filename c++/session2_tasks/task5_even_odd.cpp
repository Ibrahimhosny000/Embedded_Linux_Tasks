// ----------------------------------------------------------------------------
//               find the even and odd numbers in the array :- 
// ----------------------------------------------------------------------------



                        // take number from user to see if odd or even

// #include <iostream>

// int main(){
//     int myarray[] = {1,2,3,4,5,6,7,8,9,10};
//     int size = sizeof(myarray) / sizeof(myarray[0]);

//     std::cout << "Enter the number you want to see if odd/even" << std::endl;
//     int num;
//     std::cin >> num;
//     bool found = false;     // intialize a bool value of false

//     for( int i = 0; i < size; ++i){ // to check if the number is in the array
        
//         if ( num == myarray[i]) {
//             found = true;    // if the number is in the array the bool value will be true
            
//             if( num % 2 == 0){
//                 std::cout << num << " is an Even number in the array  "<< std::endl;
//             } 
//             else{
//                 std::cout << num << " is an Odd number in the array "<< std::endl;
//             }
            
//             break;
//         }
//     }

//     if (found == false) {   // if the number is not in the array the bool value stay false
//         std::cout << "number '"<< num << "' is not in the array " << std::endl;
//     }


// return 0;
// }

                        // see all numbers in array odd or even

#include <iostream>

int main(){

    int myarray[] = {1,2,3,4,5,6,7,8,9,10,13,14,22};
    int size = sizeof(myarray) / sizeof(myarray[0]);

    std::cout << "Even numbers are: " << std::endl;
    for( int i = 0; i < size; ++i){
        if(myarray[i] % 2 == 0 ){
            std::cout<< myarray[i] << " ";
        }
    }
    std::cout  << std::endl;
    std::cout << "Odd numbers are: " << std::endl;
    for(int i = 0; i < size; ++i){
        if( myarray[i] % 2 != 0 ){
            std::cout << myarray[i] << " ";
        }
    }
std::cout << std::endl;

return 0;
}
