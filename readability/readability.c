#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_letters(string text);
int count_words(string text);

int main(void)
{
    int sentences = 0;
    string text = get_string("Text: ");


        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }


    printf("%i %i %i", letters, words, sentences);
}















int count_words(string text)
{
     int words = 1;
     for (int i = 0, n = strlen(text); i < n; i++)
     {
        if (text[i] == ' ')
        {
            words++;
        }
     }
     return words;
}













int count_letters(string text)
{
     int letters = 0;
     for (int i = 0, n = strlen(text); i < n; i++)
     {
        if (isalpha(text[i]))
        {
            letters++;
        }
     }
     return letters;
}