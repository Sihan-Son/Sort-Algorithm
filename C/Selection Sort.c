#include <stido.h>

int main()
{
    int list[] ={8,9,5,7,6,1,3,2,4};
    int i,j,temp;
    int indexMin;

    for(i=0; i<sizeof(list)/sizeof(int)-1;i++)
    {
        indexMin = 1;
        for(j=i+1; j < sizeof(list)/sizeof(int); j++)
        {
            if(list[indexMin] > list[j])
                indexMin = j;

            temp = list[indexMin];
            list[indexMin] = list[i];
            list[i] = temp;
        }
    }

}
