// -----------------------------------------------------------------------
//             right angele triangel :-
// -----------------------------------------------------------------------

// ---------------- IF THE ENTERED VALUES ARE ANGLES ----------------


#include <iostream>
float a, b, c;
int main(){
    std::cout << "Enter three angles of a triangle to\ndetermine if it's a right angel triangle" << std::endl;
    std::cin>> a >> b >> c ;
    float sum = a + b + c;

    if (a != 0 && b != 0 && c != 0) {
        if(a == 90 || b == 90 || c == 90 ){ // one of the angles of right angle triangle must be 90
        if (sum == 180){ // three angles of triangle must be equal to 180
            std::cout << "These angles add up to\nA Right Angle Triangle" << std::endl; 
        }
        else
        {
            std::cout << "Theses angles does not add up to make a triangle" << std::endl;
        }
        }
        else if (a != 90 || b != 90 || c != 90)
        {
        if(sum == 180){
            std::cout << "This triangle is not a Right Angle Triangle" << std::endl;
        }
        else
        {
            std::cout << "Theses angles does not add up to make a triangle" << std::endl;
        }
        
        }
    
        }
    else
    {
        std::cout << "0 can't be an angle " << std::endl;
        
    }

return 0;
}



// ---------------- IF THE ENTERED VALUES ARE SIDES ---------------- 


// #include <iostream>
// float a, b, c;
// int main(){
//     std::cout << "Enter three sides to determine if\nRight Angle Triangle" << std::endl;
//     std::cin>> a >> b >> c;
//     float hyp_a = a * a;
//     float hyp_b = b * b;
//     float hyp_c = c * c;  // pythagoras theorem: hyp*2 = altitude*2 + base*2
//     if (a != 0 && b != 0 && c != 0) {
//         if (hyp_a == hyp_b + hyp_c){
//         std::cout << "This is a right angel triangle\nThe hypotenuse is "<< a << std::endl;
//         }
//         else if (hyp_b == hyp_a + hyp_c) {
//         std::cout << "This is a right angel triangle\nThe hypotenuse is "<< b << std::endl;
//         }
//         else if (hyp_c == hyp_a + hyp_b) {
//         std::cout << "This is a right angel triangle\nThe hypotenuse is "<< c << std::endl;
//         }
//         else
//         {
//         std::cout << "This is 'NOT' a Right Angle Triangle " << std::endl;
//         }
//     }
//     else
//     {
//         std::cout << "0 cant't be a side length" << std::endl;
//     }


// return 0;
// }