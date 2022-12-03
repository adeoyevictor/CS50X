#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("ERROR: Usage ./recover FILE\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    BYTE read[512];

    int count = 0;

    while (fread(read, 1, 512, input) == 512)
    {
        if (read[0] == 0xff && read[1] == 0xd8 && read[2] == 0xff && (read[3] & 0xf0) == 0xe0)
        {
            char *name = malloc(8);
            if (count == 0)
            {
                sprintf(name, "%03i.jpg", count);
                FILE *img = fopen(name, "w");
                fwrite(read, 1, 512, img);
            }
            else
            {
                fclose(name);
            }

            // free(name);
            // count++;
        }
        else
        {

        }

    }

}

// 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