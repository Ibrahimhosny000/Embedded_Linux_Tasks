// ----------------------------------------------------------------------------
//          create a function to delete a number in the array :- 
// ----------------------------------------------------------------------------

#include <iostream>

void printarray(int arr[], int size){
    for( int i = 0; i < size; ++i){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main(){
    int myarr[]={1,2,3,4,5,6,7,8,9};
    int size = sizeof (myarr) / sizeof(myarr[0]);

    std::cout << "Enter the number you want to delete from array" << std::endl;
    int DeletedNum;
    std::cin>> DeletedNum;

    std::cout << "The intial array is "<< std::endl;
    printarray(myarr, size);

    int index = -1;

    for( int i = 0; i < size; ++i){
        if(DeletedNum == myarr[i]){  // to find the index of the number to be deleted
            index = i; 
            break;
        }
    }

    
    for (int i = index; i < size - 1; i++) {
    myarr[i] = myarr[i + 1];  // shift all the array elements to the lift before the element to be deleted
    }

    size--;      // reduce the size of the array by one to delete the element
    
    std::cout << "The array after deleting the number is: "<< std::endl;
    for (int i = 0; i < size; i++) {
    std::cout << myarr[i] << " ";
    }
    std::cout << std::endl;

    if(index == -1){
        std::cout << "error NOT found" << std::endl;
    }



return 0;
}
