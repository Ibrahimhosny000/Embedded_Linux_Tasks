// ---------------------------------------------------------------
//         -check if there is any value of array is even ?
// ---------------------------------------------------------------

#include <iostream>

int main(){
    
    int array[] = {1,3,5,7,2,9,11,13,15};
    int size = sizeof(array) / sizeof(array[0]);

    bool flag = true;
    for (int i = 0; i < size; i++) {
    if (array[i] % 2 == 0) {
      flag = false;
      std::cout << "There is an even number in the array" << std::endl;
      break;
    }
    }
 
    if (flag) {
    std::cout << "All the elements in the array are odd" << std::endl;
    }

return 0;
}

