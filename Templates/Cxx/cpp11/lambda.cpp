
/* =============================================================================
 * 
 * Title:       
 * Author:      
 * License:     
 * Description: 
 * 
 * 
 * =============================================================================
 */
 
 
 
#include <iostream>
#include <vector>

#ifndef EXIT_SUCCESS
    #define EXIT_SUCCESS 0
#endif

#define COUNT 1024

using namespace std;

int main(int argc, char** argv) {
    vector<double> nummap;
    
    cout << "Filling vector with numbers ... " << endl;
    
    // Define LAMBDA
    double (*getNumber)(int) = [](int a) { return (double)a*(double)a; };
    // Alternative: auto getNumber = [] (int a) { ... };
    
    
    for(int i=0;i<COUNT;i++) {
    	double number = getNumber(i);
    	nummap.push_back(number);
    	cout << number << endl;
    }
    
    cout << "Bye" << endl;
    
    return EXIT_SUCCESS;
}
