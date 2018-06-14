#include <stdio.h>

int main()
{
    int list[] = {2,3,5,9,7,1,6,12,48,56};
    int i,j;
    int temp;

    for(i = 0; i<sizeof(list)/sizeof(int); i++)
    {
        for(j = 1; j < sizeof(list)/sizeof(int) - 1; j++)
        {
            if(list[j-1] > list[j])
            {
                temp = list[j-1];
                list[j-1] = list[j];
                list[j] = temp;
            }
        }
    }
}