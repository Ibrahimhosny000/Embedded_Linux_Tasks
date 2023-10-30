// ----------------------------------------------------------------------------
//          create a function to find the maximum number of array :- 
// ----------------------------------------------------------------------------

// #include <iostream>

// int main(){

//     int myarr[]={10,20,20,50,90,333,1,14,333,22};
    
//     int size = sizeof(myarr) / sizeof(myarr[0]); 
    
//     int max = myarr[0];                // declare the first element as the maximum

//     for( int i = 0; i < size; ++i){   // loops over the array
//         if(myarr[i] > max){           // compair each element in array to the declarid max
//             max = myarr[i];           // if the elemet > max it declairs it as the max
//         }
//     }
//     std::cout << "Max number is array is --> " << max <<std::endl;
    
// return 0;
// }


                // ---------------------------------------
                //          another way by sort
                // ---------------------------------------
#include <iostream>
#include <algorithm>

int main(){
    int myarr[]={3,2,55,3,16,3,15,46};
    int size = sizeof(myarr) / sizeof(myarr[0]);

    std::cout << "From array { ";
    for(int i = 0; i < size; ++i){
        std::cout << myarr[i] << " ";
    }
    std::cout << "}" << std::endl;

    std::sort(myarr,myarr+size);
    std::cout << "max number is : "<<myarr[size-1] << std::endl;
return 0;
}
