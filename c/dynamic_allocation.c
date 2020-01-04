#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char *str;
  
  /* Initial memory allocation */
  str = (char *) malloc(6);
  strcpy(str, "adela");
  printf("String = %s, Address = %p\n", str, str);

  /* Reallocating memory */
  str = (char *) realloc(str, 17);
  strcat(str, ".love");
  printf("String = %s, Address = %p\n", str, str);

  free(str);
  return (0);
}
