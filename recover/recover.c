#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("ERROR: Usage ./recover FILE\n");
        return 1;
    }

    FILE *f = fopen(argv[1], 'r');

}