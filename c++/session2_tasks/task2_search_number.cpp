// ----------------------------------------------------------------------------
//          create a function to search for a number in the array :- 
// ----------------------------------------------------------------------------

#include <iostream>

int main(){
    int arr[]={1,2,3,4,5,6,7,8,9};
    int size = sizeof (arr) / sizeof(arr[0]);

    std::cout << "Enter the number you want to search for" << std::endl;
    int num;
    std::cin >> num;

    bool found = false;     // intialize a bool value of false
    for( int i = 0; i < size; ++i){
        if ( num == arr[i]) {
            found = true;    // if the number is in the array the bool value will be true
            std::cout <<"your number: " << num << " is in the array at index " << i <<std::endl;
            break;
        }
    }
    if (found == false) {   // if the number is not in the array the bool value stay false
        std::cout << "NOT found" << std::endl;
    }

    return 0;
}
