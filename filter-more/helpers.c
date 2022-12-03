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


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            float bluex = 0;
            float greenx = 0;
            float redx = 0;
            float bluey = 0;
            float greeny = 0;
            float redy = 0;

            if (i == 0 && j == 0)
            {
                  bluex = bluex + (newImage[i][j + 1].rgbtBlue * 2) + (newImage[i + 1][j + 1].rgbtBlue * 1);
                  greenx = greenx + (newImage[i][j + 1].rgbtGreen * 2) + (newImage[i + 1][j + 1].rgbtGreen * 1);
                  redx = redx + (newImage[i][j + 1].rgbtRed * 2) + (newImage[i + 1][j + 1].rgbtRed * 1);
                  bluey = bluey +  (newImage[i + 1][j].rgbtBlue * 2) + (newImage[i + 1][j + 1].rgbtBlue * 1);
                  greeny = greeny +  (newImage[i + 1][j].rgbtGreen * 2) + (newImage[i + 1][j + 1].rgbtGreen * 1);
                  redy = redy +  (newImage[i + 1][j].rgbtRed * 2) + (newImage[i + 1][j + 1].rgbtRed * 1);

            }
            else if (i == 0 && j == width - 1)
            {
                 bluex = bluex + (newImage[i][j - 1].rgbtBlue * -2)  +  (newImage[i + 1][j - 1].rgbtBlue * - 1);
                 greenx = greenx + (newImage[i][j - 1].rgbtGreen * -2)  +  (newImage[i + 1][j - 1].rgbtGreen * - 1);
                 redx = redx + (newImage[i][j - 1].rgbtRed * -2)  +  (newImage[i + 1][j - 1].rgbtRed * - 1);
                 bluey = bluey + (newImage[i + 1][j - 1].rgbtBlue * 1) + (newImage[i + 1][j].rgbtBlue * 2);
                 greeny = greeny + (newImage[i + 1][j - 1].rgbtGreen * 1) + (newImage[i + 1][j].rgbtGreen * 2);
                 redy = redy + (newImage[i + 1][j - 1].rgbtRed * 1) + (newImage[i + 1][j].rgbtRed * 2);
            }
            else if (i == height - 1 && j == 0)
            {
                bluex = bluex +  (newImage[i][j + 1].rgbtBlue * 2)  + (newImage[i - 1][j + 1].rgbtBlue * 1);
                greenx = greenx +  (newImage[i][j + 1].rgbtGreen * 2)  + (newImage[i - 1][j + 1].rgbtGreen * 1);
                redx = redx +  (newImage[i][j + 1].rgbtRed * 2)  + (newImage[i - 1][j + 1].rgbtRed * 1);
                bluey = bluey +  (newImage[i - 1][j].rgbtBlue * -2) + (newImage[i - 1][j + 1].rgbtBlue * -1);
                greeny = greeny +  (newImage[i - 1][j].rgbtGreen * -2) + (newImage[i - 1][j + 1].rgbtGreen * -1);
                redy = redy +  (newImage[i - 1][j].rgbtRed * -2) + (newImage[i - 1][j + 1].rgbtRed * -1);
            }
            else if (i == height - 1 && j == width - 1)
            {
                bluex = bluex +  (newImage[i][j - 1].rgbtBlue * -2) +  (newImage[i - 1][j - 1].rgbtBlue * -1);
                greenx = greenx +  (newImage[i][j - 1].rgbtGreen * -2) +  (newImage[i - 1][j - 1].rgbtGreen * -1);
                redx = redx +  (newImage[i][j - 1].rgbtRed * -2) +  (newImage[i - 1][j - 1].rgbtRed * -1);
                bluey = bluey + (newImage[i - 1][j - 1].rgbtBlue * -1) + (newImage[i - 1][j].rgbtBlue * -2);
                greeny = greeny + (newImage[i - 1][j - 1].rgbtGreen * -1) + (newImage[i - 1][j].rgbtGreen * -2);
                redy = redy + (newImage[i - 1][j - 1].rgbtRed * -1) + (newImage[i - 1][j].rgbtRed * -2);
            }
            else if (i == 0)
            {
                  bluex = bluex + (newImage[i][j - 1].rgbtBlue * -2) + (newImage[i][j + 1].rgbtBlue * 2) +  (newImage[i + 1][j - 1].rgbtBlue * -1)  + (newImage[i + 1][j + 1].rgbtBlue * 1);
                  greenx = greenx + (newImage[i][j - 1].rgbtGreen * -2) + (newImage[i][j + 1].rgbtGreen * 2) +  (newImage[i + 1][j - 1].rgbtGreen * -1)  + (newImage[i + 1][j + 1].rgbtGreen * 1);
                  redx = redx + (newImage[i][j - 1].rgbtRed * -2) + (newImage[i][j + 1].rgbtRed * 2) +  (newImage[i + 1][j - 1].rgbtRed * -1)  + (newImage[i + 1][j + 1].rgbtRed * 1);

                  bluey = bluey + (newImage[i + 1][j - 1].rgbtBlue * 1) + (newImage[i + 1][j ].rgbtBlue * 2) + (newImage[i + 1][j + 1].rgbtBlue * 1);
                  greeny = greeny + (newImage[i + 1][j - 1].rgbtGreen * 1) + (newImage[i + 1][j ].rgbtGreen * 2) + (newImage[i + 1][j + 1].rgbtGreen * 1);
                  redy = redy + (newImage[i + 1][j - 1].rgbtRed * 1) + (newImage[i + 1][j ].rgbtRed * 2) + (newImage[i + 1][j + 1].rgbtRed * 1);
            }
            else if (j == 0)
            {
                 bluex = bluex +  (newImage[i][j + 1].rgbtBlue * 2)  + (newImage[i - 1][j + 1].rgbtBlue * 1) + (newImage[i + 1][j + 1].rgbtBlue * 1);
                 greenx = greenx +  (newImage[i][j + 1].rgbtGreen * 2)  + (newImage[i - 1][j + 1].rgbtGreen * 1) + (newImage[i + 1][j + 1].rgbtGreen * 1);
                 redx = redx +  (newImage[i][j + 1].rgbtRed * 2)  + (newImage[i - 1][j + 1].rgbtRed * 1) + (newImage[i + 1][j + 1].rgbtRed * 1);
                 bluey = bluey + (newImage[i - 1][j].rgbtBlue * -2) + (newImage[i - 1][j + 1].rgbtBlue * -1) + (newImage[i + 1][j].rgbtBlue * 2) + (newImage[i + 1][j + 1].rgbtBlue * 1);
                 greeny = greeny + (newImage[i - 1][j].rgbtGreen * -2) + (newImage[i - 1][j + 1].rgbtGreen * -1) + (newImage[i + 1][j].rgbtGreen * 2) + (newImage[i + 1][j + 1].rgbtGreen * 1);
                 redy = redy + (newImage[i - 1][j].rgbtRed * -2) + (newImage[i - 1][j + 1].rgbtRed * -1) + (newImage[i + 1][j].rgbtRed * 2) + (newImage[i + 1][j + 1].rgbtRed * 1);
            }
            else if (i == height - 1)
            {
                bluex = bluex + (newImage[i][j - 1].rgbtBlue * -2) + (newImage[i][j + 1].rgbtBlue * 2) + (newImage[i - 1][j - 1].rgbtBlue * -1) + (newImage[i - 1][j + 1].rgbtBlue * 1);
                greenx = greenx + (newImage[i][j - 1].rgbtGreen * -2) + (newImage[i][j + 1].rgbtGreen * 2) + (newImage[i - 1][j - 1].rgbtGreen * -1) + (newImage[i - 1][j + 1].rgbtGreen * 1);
                redx = redx + (newImage[i][j - 1].rgbtRed * -2) + (newImage[i][j + 1].rgbtRed * 2) + (newImage[i - 1][j - 1].rgbtRed * -1) + (newImage[i - 1][j + 1].rgbtRed * 1);
                bluey = bluey + (newImage[i - 1][j - 1].rgbtBlue * -1) + (newImage[i - 1][j].rgbtBlue * -2) + (newImage[i - 1][j + 1].rgbtBlue * -1);
                greeny = greeny + (newImage[i - 1][j - 1].rgbtGreen * -1) + (newImage[i - 1][j].rgbtGreen * -2) + (newImage[i - 1][j + 1].rgbtGreen * -1);
                redy = redy + (newImage[i - 1][j - 1].rgbtRed * -1) + (newImage[i - 1][j].rgbtRed * -2) + (newImage[i - 1][j + 1].rgbtRed * -1);
            }
            else if (j == width - 1 )
            {
                bluex = bluex +  (newImage[i][j - 1].rgbtBlue * -2) + (newImage[i - 1][j - 1].rgbtBlue * -1) + (newImage[i + 1][j - 1].rgbtBlue * -1);
                greenx = greenx +  (newImage[i][j - 1].rgbtGreen * -2) + (newImage[i - 1][j - 1].rgbtGreen * -1) + (newImage[i + 1][j - 1].rgbtGreen * -1);
                redx = redx +  (newImage[i][j - 1].rgbtRed * -2) + (newImage[i - 1][j - 1].rgbtRed * -1) + (newImage[i + 1][j - 1].rgbtRed * -1);
                bluey = bluey + (newImage[i - 1][j - 1].rgbtBlue * -1) + (newImage[i - 1][j].rgbtBlue * -2) + (newImage[i + 1][j - 1].rgbtBlue * 1) + (newImage[i + 1][j].rgbtBlue * 2);
                greeny = greeny + (newImage[i - 1][j - 1].rgbtGreen * -1) + (newImage[i - 1][j].rgbtGreen * -2) + (newImage[i + 1][j - 1].rgbtGreen * 1) + (newImage[i + 1][j].rgbtGreen * 2);
                redy = redy + (newImage[i - 1][j - 1].rgbtRed * -1) + (newImage[i - 1][j].rgbtRed * -2) + (newImage[i + 1][j - 1].rgbtRed * 1) + (newImage[i + 1][j].rgbtRed * 2);
            }
            else
            {
                bluex = bluex + (newImage[i][j - 1].rgbtBlue * -2) + (newImage[i][j + 1].rgbtBlue * 2) + (newImage[i - 1][j - 1].rgbtBlue * -1) + (newImage[i + 1][j - 1].rgbtBlue * -1) + (newImage[i - 1][j + 1].rgbtBlue * 1) + (newImage[i + 1][j + 1].rgbtBlue * 1);

                greenx = greenx + (newImage[i][j - 1].rgbtGreen * -2) + (newImage[i][j + 1].rgbtGreen * 2) + (newImage[i - 1][j - 1].rgbtGreen * -1) + (newImage[i + 1][j - 1].rgbtGreen * -1) + (newImage[i - 1][j + 1].rgbtGreen * 1) + (newImage[i + 1][j + 1].rgbtGreen * 1);

                redx = redx + (newImage[i][j - 1].rgbtRed * -2) + (newImage[i][j + 1].rgbtRed * 2) + (newImage[i - 1][j - 1].rgbtRed * -1) + (newImage[i + 1][j - 1].rgbtRed * -1) + (newImage[i - 1][j + 1].rgbtRed * 1) + (newImage[i + 1][j + 1].rgbtRed * 1);

                bluey = bluey + (newImage[i - 1][j - 1].rgbtBlue * -1) + (newImage[i - 1][j].rgbtBlue * -2) + (newImage[i - 1][j + 1].rgbtBlue * -1) + (newImage[i + 1][j - 1].rgbtBlue * 1) + (newImage[i + 1][j ].rgbtBlue * 2) + (newImage[i + 1][j + 1].rgbtBlue * 1);

                greeny = greeny + (newImage[i - 1][j - 1].rgbtGreen * -1) + (newImage[i - 1][j].rgbtGreen * -2) + (newImage[i - 1][j + 1].rgbtGreen * -1) + (newImage[i + 1][j - 1].rgbtGreen * 1) + (newImage[i + 1][j ].rgbtGreen * 2) + (newImage[i + 1][j + 1].rgbtGreen * 1);

                redy = redy + (newImage[i - 1][j - 1].rgbtRed * -1) + (newImage[i - 1][j].rgbtRed * -2) + (newImage[i - 1][j + 1].rgbtRed * -1) + (newImage[i + 1][j - 1].rgbtRed * 1) + (newImage[i + 1][j ].rgbtRed * 2) + (newImage[i + 1][j + 1].rgbtRed * 1);

            }

            int blue = round(sqrt((bluex * bluex) + (bluey * bluey)));
            int green = round(sqrt((greenx * greenx) + (greeny * greeny)));
            int red =  round(sqrt((redx * redx) + (redy * redy)));

            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            image[i][j].rgbtBlue = blue;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtRed = red;


        }
    }

    return;
}


