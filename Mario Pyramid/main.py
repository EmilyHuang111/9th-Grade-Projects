
#include <stdio.h>

int main(void)
{
    int height;
    do 
      {
        printf("Height: ");
        scanf("%d", &height);
      }
    while (height < 1 || height > 8);
    
      

    if (height == 1)
    {
        printf("#");
    }

    else if (height == 2)

    {
        printf(" #\n");
        printf("##");
    }

    else if (height == 3)

    {
        printf("  #\t");
        printf(" ##\t");
        printf("###");
    }
    else if (height == 4)

    {
        printf("   #\n");
        printf("  ##\n");
        printf(" ###\n");
        printf("####");
    }

    else if (height == 5)

    {
        printf("    #\n");
        printf("   ##\n");
        printf("  ###\n");
        printf(" ####\n");
        printf("#####");
    }

    else if (height == 6)

    {
        printf("     #\n");
        printf("    ##\n");
        printf("   ###\n");
        printf("  ####\n");
        printf(" #####\n");
        printf("######");
    }

    else if (height == 7)
    {
      printf("      #\n");
      printf("     ##\n");
      printf("    ###\n");
      printf("   ####\n");
      printf("  #####\n");
      printf(" ######\n");
      printf("#######");
    }

    else if (height == 8)

    {
      printf("       #\n");
      printf("      ##\n");
      printf("     ###\n");
      printf("    ####\n");
      printf("   #####\n");
      printf("  ######\n");
      printf(" #######\n");
      printf("########");
    }
}
