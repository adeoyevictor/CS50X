#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    
}



int count_sentences(string text)
{
     int sentences = 0;
     for (int i = 0, n = strlen(text); i < n; i++)
     {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
     }
     return sentences;
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