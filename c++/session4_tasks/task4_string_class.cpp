// ---------------------------------------------------------------
//               -string class which has Members
// ---------------------------------------------------------------

#include <iostream>
#include <string>
class string {
    private:
        
        std::string Name;

    public:
       
        void setname(){               // setter
            std::cout << "Enter a string" << std::endl;
            std::cin>> Name;
        }

        std::string getname(){        // getter
            return Name;
        }

        int getlenght(){
            return Name.length();
            
        }

};

int main(){
    string d;
    d.setname();
    std::cout << "The string is \"" << d.getname() <<  "\"" <<std::endl;
    std::cout << "The lenght of string " << d.getname() << " is "<< d.getlenght() <<std::endl;

return 0;
}