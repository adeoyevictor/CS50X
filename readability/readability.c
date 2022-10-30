#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int letters = 0;
    int words = 0;
    int sentences = 0;
    string text = get_string("Text: ");
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            letters++;
        }
        else if (text[i] == ' ')
        {
            words++;
        }
        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    printf("%i %i %i", letters, words, sentences);
}