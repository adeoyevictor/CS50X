#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
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
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2 ; j++)
        {
            RGBTRIPLE temp = image[i][j];

            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE newImage[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            newImage[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            int a;
            int b;
            int c;
            int d;

            if (i == 0)
            {
                a = 0;
                b = i + 1;
            }
            else if (i == height - 1)
            {
                b = height - 1;
                a = height - 2;
            }
            else
            {
                a = i - 1;
                b = i + 1;
            }
            if (j == 0)
            {
                c = 0;
                d = j + 1;
            }
            else if (j == width - 1)
            {
                d = width - 1;
                c = width - 2;
            }
            else
            {
                c = j - 1;
                d = j + 1;
            }
            int blue = 0;
            int green = 0;
            int red = 0;
            int count = 0;
            for (int s = a; s <= b; s++)
            {
                for (int t = c; t <= d; t++)
                {
                    blue += newImage[s][t].rgbtBlue;
                    green += newImage[s][t].rgbtGreen;
                    red += newImage[s][t].rgbtRed;
                    count++;
                }
            }
            image[i][j].rgbtBlue = (int) round((double) blue / count);
            image[i][j].rgbtGreen = (int) round((double) green / count);
            image[i][j].rgbtRed = (int) round((double) red / count);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE newImage[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            newImage[i][j] = image[i][j];
        }
    }

    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

      for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {

            int redx = 0;
            int greenx = 0;
            int bluex = 0;
            int redy = 0;
            int greeny = 0;
            int bluey = 0;

            for (int s = -1; s < 2; s++)
            {
                for (int t = -1; t < 2; t++)
                {
                    if (i + s < 0 || i + s >= height)
                    {
                        continue;
                    }
                    if (j + t < 0 || j + t >= width)
                    {
                        continue;
                    }
                    redx += newImage[i + k][j + l].rgbtRed * Gx[k + 1][l + 1];
                    greenx += newImage[i + k][j + l].rgbtGreen * Gx[k + 1][l + 1];
                    bluex += newImage[i + k][j + l].rgbtBlue * Gx[k + 1][l + 1];
                    redy += newImage[i + k][j + l].rgbtRed * Gy[k + 1][l + 1];
                    greeny += newImage[i + k][j + l].rgbtGreen * Gy[k + 1][l + 1];
                    bluey += newImage[i + k][j + l].rgbtBlue * Gy[k + 1][l + 1];
                }
            }
        }
    }
    return;
}


