#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if(argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    if (strlen(argv[1]) != 26){
        printf("Length must be 26\n");
        return 1;
    }
    for(int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if(isalpha(argv[1][i]))
        {

        }
        else
        {
            printf("Invalid Key\n");
            return 1;
        }
        for(int j = 0, m = strlen(argv[1]); j < m; j++)
        {
            if(i == j)
            {
                continue;
            }
            if(argv[1][i] == argv[1][j])
            {
                printf("Invalid Key\n");
                return 1;
            }
        }
    }

    string plain = get_string("plaintext: ");
    char cypher[strlen(argv[1])];

    for (int i = 0, n = strlen(plain); i < n; i++ )
    {
        if(isalpha(plain[i]))
        {
            if(islower(plain[i]))
            {
                int index = plain[i] - 97;
                cypher[i] = tolower(argv[1][index]);
            }
            if(isupper(plain[i]))
            {
                int index = plain[i] - 65;
                cypher[i] = toupper(argv[1][index]);
            }
        }
        else
        {
            cypher[i] = plain[i];
        }
    }
    printf("ciphertext: %s\n", cypher);
}