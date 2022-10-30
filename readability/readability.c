#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int letters;
    int words;
    int sentences;
    string text = get_string("Text: ");
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            
        }
    }
}