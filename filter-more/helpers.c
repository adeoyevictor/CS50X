#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            double avg  = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            avg = (int) avg;
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
   for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int tempBlue = image[i][j].rgbtBlue;
            int tempRed = image[i][j].rgbtRed;
            // int tempGreen = image[i][j].rgbtGreen;
            int secBlue = image[i][width - (j + 1)].rgbtBlue;
            int secRed = image[i][width - (j + 1)].rgbtRed;
            // int secGreen = image[i][width - (j + 1)].rgbtGreen;
            image[i][j].rgbtBlue = secRed ;
            image[i][j].rgbtRed = secBlue ;
            image[i][width - (j + 1)].rgbtBlue = tempRed;
            image[i][width - (j + 1)].rgbtRed = tempBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
