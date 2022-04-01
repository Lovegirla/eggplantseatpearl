#include <iostream>
#include "Router.h"
#include "Setting.h"
using namespace std;

Setting setting;

int main(int argc, char *argv[]){

    cout << "Handling Task One: CLOCK SRC-TAPS ROUTING " << endl;
    cout << "Input file name" << argv[1] << endl;
    cout << "Output file name" << argv[2] << endl;
    
    string input_file_name(argv[1]);
    string output_file_name(argv[2]);
    
    setting.input_file_name= input_file_name;
    setting.output_file_name = output_file_name;

    Router router;
    router.init();
    router.route();
    router.buildSolution();
    router.writeSolution();
    
    cout << "End of Process" << endl;
    return 0;
}