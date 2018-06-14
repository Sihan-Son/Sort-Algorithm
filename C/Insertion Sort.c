#include <stido.h>


int main()
{
    int list = {40,30,70,60,50,10,20};

    int i, key, j;

    for(i = 0; i < sizeof(list)/sizeof(int); i++)
    {
        j = i-1;
        key = list[i];

        
        while(list[j] > key && j >= 0){
            x[j+1]  = x[j];
            j = j - 1;
        }
        x[j+1] =  key;
    }    
}