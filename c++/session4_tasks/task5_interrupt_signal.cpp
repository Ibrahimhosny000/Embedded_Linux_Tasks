// ----------------------------------------------------------
//         -handle interrupt signal like (ctrl+c)
// ----------------------------------------------------------

#include <iostream>
#include <signal.h> 

void handler(int signal) {
    std::cout << std::endl;
    std::cout << "Ctrl+C command is pressed " << std::endl;
    std::cout << "EXIT loop " << std::endl;
  exit(0);
}

int main() {

    std::cout<< "Press ctrl^c to exit " << std::endl;
    signal(SIGINT, handler);

  while (true) {}   // infinite loop to keep code on going
  return 0;
}

