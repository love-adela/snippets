#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char *str;
  
  /* Initial memory allocation */
  str = (char *) malloc(6);
  strcpy(str, "adela");
  printf("String = %s, Address = %p\n", str, str);

  /* Reallocating memory: 크기를 늘리거나 줄입니다. */
  str = (char *) realloc(str, 17);
  strcat(str, ".love");
  printf("String = %s, Address = %p\n", str, str);

  free(str);
  /* 프로그램이 꺼질 때까지 메모리 누수가 발생한다. 따라서 더이상 쓰지 않을 때 바로 deallocate을 해야 합니다.*/
  return (0);
}
