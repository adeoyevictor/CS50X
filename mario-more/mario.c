#include <cs50.h>
#include <stdio.h>

void pr(void)
{
    printf("#");
}

void printHashtag(int i)
{
    for(int j = 1; j < i+1 ;i++)
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