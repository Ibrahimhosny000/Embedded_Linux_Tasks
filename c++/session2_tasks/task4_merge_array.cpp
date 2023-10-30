// ----------------------------------------------------------------------------
//          create a function to merge two arrays together :- 
// ----------------------------------------------------------------------------


                      // for fixed arrays entered by author
// #include <iostream>

// int main(){

//     int array1[] = {1,2,3,4,5,6,7,8};
//     int array2[] = {10,20,30,40,50,60,70,80};

//     int size1 = sizeof(array1) / sizeof(array1[0]);
//     int size2 = sizeof(array2) / sizeof(array2[0]);

//     int array3[ size1 + size2 ];

//     int i = 0, j = 0, k = 0;

//     while ( i < size1 ){
//         array3[k++] = array1[i++]; // insert elements of array1 to array3
//     }
//     while ( j < size2) {
//         array3[k++] = array2[j++]; // insert elements of array2 to array3 
//     }

//     std::cout << "array after merging array1 + array2 is: " << std::endl; 
//     for( int i = 0; i < size1 + size2; ++i){
//         std::cout << array3[i] << " ";
//     }
//     std::cout << std::endl;


// return 0;
// }


                          // for arrays entered by the user

#include<iostream>

int main()
{
    int fisrtarr[10], Secondarr[10], mergearr[20];
	int sizeone, sizetwo, i, k;

    std::cout<<"Enter the size for first array\nMAX SIZE '10' : ";
    std::cin>>sizeone;

    if ( sizeone <= 10){   // to make sure that entered size does not exced limit
        std::cout<<"Enter "<<sizeone<<" elements for first array" << std::endl;
        
        for(i=0; i<sizeone; i++){
        std::cin>>fisrtarr[i];
        mergearr[i] = fisrtarr[i];
    }

    k = i; // to make the elements of second array after the first

    std::cout<<"Enter the size for second array\nMAX SIZE '10' : ";
    std::cin>>sizetwo;

    if( sizetwo <= 10){
        std::cout<<"Enter "<<sizetwo<<" elements for Second Array: ";
        
        for(i=0; i<sizetwo; i++){
        std::cin>>Secondarr[i];
        mergearr[k] = Secondarr[i];
        k++;
    }
    
        std::cout<<"Array after merging array1 + array2 is: "<< std::endl;
    for(i=0; i<k; i++){
        std::cout<<mergearr[i]<< " ";
    }
    std::cout << std::endl;

    }
    else{
        std::cout << "size not avilable" << std::endl;
    }
    }
    else{
        std::cout << "size not avilable" << std::endl;
    }

return 0;
}
