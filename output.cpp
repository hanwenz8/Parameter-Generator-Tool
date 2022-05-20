// File to store generated C++ code
#include <iostream>
class Foo {
    private:
        int age;
        std::string gender;
    public:
        Foo(int a=0, std::string g=" ") : age(a), gender(g) {}
        int get_age() const {
            return age;
        }
        void set_age(int a) {
            age = a;
        }
};

int main () {
    std::cout <<"parameter generator demo" << std::endl;
    std::cout << "This is a file that contains variable for parameter generator demo" << std::endl;
    Foo hz(108, "male");
    int age = hz.get_age();
    Foo fsx(25, "famale");
    int age = fsx.get_age();
    return 0;
}
