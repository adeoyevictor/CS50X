#include <cs50.h>
#include <stdio.h>

void ht(int i)
{

}

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while(height  < 1 || height > 8);
    
    for(int i = 1; i <= height; i++)
    {

    }
}