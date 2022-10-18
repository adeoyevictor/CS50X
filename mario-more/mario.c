#include <cs50.h>
#include <stdio.h>

void printSpaces(int i)
{
    for(int j = i; j > 0 ; j--)
    {
        printf(" ");
    }
}

void printHashTags(int i)
{
    for(int j = i; j > 0 ; j--)
    {
        printf("#");
    }
}

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while(height  < 1 || height > 10);

    for(int i = 1; i <= height; i++)
    {
        printSpaces(height - i);
        printHashTags(i);
        printSpaces(2);
        printHashTags(i);
        printf("\n");

    }
}