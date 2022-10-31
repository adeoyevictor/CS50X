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
    if (strlen(argv[0]) != 26){
        printf("Length must be 26");
        return 1;
    }
    for(int i = 0, n = strlen(argv[0]); i < n; i++)
    {
        if(isalpha(argv[0][i]))
        {

        }
        else
        {
            printf("Invalid Key\n");
            return 1;
        }
        for(int j = 0, m = strlen(argv[0]); j < m; j++)
        {
            if(i == j)
            {
                continue;
            }
            if(argv[0][i] == argv[0][j])
            {
                printf("Invalid Key\n");
                return 1;
            }
        }
    }

    string plain = get_string("plaintext: ");

    

}