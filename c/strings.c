#include <stdio.h>
#include <string.h>

int main() {
  char first_name[] = "Boe";
  char last_name[] = "John";
  char name[100];

  last_name[0] = 'B'; // "John"을 "Bohn"으로 바꿨음
  printf("%s\n", last_name);
  sprintf(name, "%s %s", first_name, last_name);
  if (strncmp(name, "John Boe", 100) == 0) {
    printf("Done!\n");
  }
  name[0]= '\0';
  strncat(name, first_name, 4);
  strncat(name, last_name, 20);
  printf("%s\n", name);
  return 0;
}

