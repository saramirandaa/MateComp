#include <iostream>
#include <cmath>
using namespace std;



void divisores(int a, int b) {
    int q = 0, r = 0;
    if (a != 0) 
    {
        r = abs(a);
        q = 0;
        while(r>=b)
        {
            r = r - b;
            q++;
        }
        if (a>0)
        {
            q = q;
            r = r;
        }else if (r==0)
        {
            q = -q;
            r = r;
        }
        else
        {
            q = -q-1;
            r = b-1;
        }
        
    }
    cout<<"  __"<<q<<"__"<<endl;
    cout<<b<<"|"<<a<<endl;
    cout<<"    "<<r<<endl;
    cout<<"\ncociente:"<<q<<" residuo:"<<r<<endl;
    
}

int main() {
    divisores(87420,13);
    return 0;
}