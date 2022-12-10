// Implements a dictionary's functionality
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cs50.h>
#include <strings.h>
#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1125;
unsigned int no = 0;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int idx = hash(word);
    node *n = table[idx];
    for (node *tmp = n; tmp != NULL; tmp = tmp->next)
    {
        if (strcasecmp(tmp -> word, word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int total = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (isalpha(word[i]))
        {
            total += toupper(word[i]) - 'A';
        }
    }
    // TODO: Improve this hash function
    return total;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];
    while (fscanf(file, "%s", buffer) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n -> word, buffer);
        int idx = hash(n -> word);

        node *start = table[idx];
        if (start == NULL)
        {
            table[idx] = n;
        }
        else
        {
            n -> next = table[idx];
            table[idx] = n;
        }
        no++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    return no;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        do
        {
            node *tmp = cursor;
            cursor = cursor -> next;
            free(tmp);
        }
        while (cursor != NULL);
    }
    return true;
}

