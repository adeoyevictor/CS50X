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

    char *name = malloc(8 * sizeof(char));

    FILE *img = NULL;

    while (fread(read, sizeof(BYTE) * 512, 1, input) == 1)
    {
        if (read[0] == 0xff && read[1] == 0xd8 && read[2] == 0xff && (read[3] & 0xf0) == 0xe0)
        {

            if (count == 0)
            {
                sprintf(name, "%03i.jpg", count);
                img = fopen(name, "w");
                fwrite(read, sizeof(BYTE) * 512, 1, img);
                count++;
            }
            else
            {
                fclose(img);
                sprintf(name, "%03i.jpg", count);
                img = fopen(name, "w");
                fwrite(read, sizeof(BYTE) * 512, 1, img);
                count++;
            }

        }
        else
        {
            if (count == 0)
            {
                continue;
            }
            fwrite(read, sizeof(BYTE) * 512, 1, img);
        }

    }
    fclose(input);
    fclose(img);
    free(name);
    return 0;

}

// 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

// pk_15c0708091de4f15a7b9d865628b35f7

submit50 cs50/problems/2022/python/indoor