/**
 * conditions.c
 *
 * Josh Kaplan
 * jk@ucf.edu
 *
 * Here is an example of if/else conditions in C.
 */

#include <stdio.h>

int main()
{
    int x = 10;

    if (x % 2 == 0)
    {
        printf("You entered an even number!\n");
    }
    else if (x < 10)
    {
        printf("x is less than 10!\n");
    }
    else if (x > 10 && x < 20)
    {
        printf("x between 10 and 20!\n");
    }
    else
    {
        printf("You entered an odd number!\n");
    }
}