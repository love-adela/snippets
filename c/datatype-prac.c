/* printf()와 scanf() 연습 */
#include <stdio.h>

int main(void) {
  // float 형 
  printf("---------------------\n");
  printf("float형 연습\n");
  printf("%f\n", 3/2.0);
  printf("%.2f \n", 3/2.0);
  printf("%8.2f \n", 12.34567);

  // 정수형
  printf("---------------------\n");
  printf("int형 연습\n");
  printf("%d", 1+2);
  printf("\n");
  printf("%d %d %d", 1, 2, 3);

  printf("%8d \n", 12345);
  printf("%8.4d\n", 123);
  printf("%08d \n", 12345*1000);
  printf("%08d \n", 125);

  // scanf()
  printf("---------------------\n");
  int iData =9;
  printf("정수를 하나 입력하세요:");
  scanf("%d", &iData);
  printf("입력한 정수: %d", iData);
  return 0;
}
