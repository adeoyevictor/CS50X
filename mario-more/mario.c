#include <cs50.h>
#include <stdio.h>

void printSpaces(int i)
{
    for(int j = i; j > 0 ; j--)
    {
        print(" ");
    }
}

void printHashTags(int i)
{
    for(int j = i; j > 0 ; j--)
    {
        print("#");
    }
}

void printHashtag(int i)
{
    for(int j = 1; j < i+1 ;j++)
    {
        pr();
    }
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
        printHashtag(i);
    }
}