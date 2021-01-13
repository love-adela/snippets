#include <stdio.h>
#define PI 3.141592
#define FREEZING_POINT 32
#define EXCHANGE_RATE 1094.61
#define LAST_DAY 31
#define DICE 6
#define LOGARITHM 2.71828
#define ROOT2 1.414141
#define ROOM 3.31
#define INCH_TO_CM 2.54
#define GRAPE_CALORIE 60

int main(void) { 
  // 1. 원주율 구하기 
  int radius = 4;
  float circumference = 2 * PI * radius;
  printf("1. 반지름 길이 4인 원주율은 %f \n", circumference);
  
  // 2. 어는점으로 섭씨 이용해서 화씨 구하기
  float fahrenheit, celcius;
  printf("2. 변환하려는 온도를 섭씨로 입력하세요: ");
  scanf("%f", &celcius);
  fahrenheit = (9.0f / 5.0f) * celcius + FREEZING_POINT;
  printf("변환된 화씨 온도는 %.2f \n", fahrenheit);

  // 3. 미국 달러 환율
  int number;
  printf("3. 갖고 있는 달러 값을 알려주세요: ");
  scanf("%d", &number);
  float total = EXCHANGE_RATE * number;
  printf("현재 지갑에는 %f 원 있습니다.\n", total);

  // 4. '1', '3', '5', '7,' '8', '10', '12'월의 마지막 날짜
  int month;
  printf("4. 이번 달을 숫자로 입력하세용: ");
  scanf("%d", &month);
  if (month == 1 | month == 3 | month == 5 | month == 7 | month == 8 | month == 10 | month == 12) {
    printf("입력하신 달의 마지막 날짜는: %d\n", LAST_DAY);
  } 
  else {
    printf("입력하신 달의 마지막 날짜는 31일이 아닙니다.\n");
  }

  // 5. 모든 수 주사위 눈으로 표현하기
  int numberDice;
  printf("5. 정수를 입력해주세요. 주사위로 표현하기 위해 6에 대한 나머지가 출력됩니다:");
  scanf("%d", &numberDice);
  printf("나머지는 %d\n", numberDice % 6);

  // 6.자연로그 상수 변환하기
  int valueLog;
  printf("6. 자연로그에 곱할 정수를 입력하세요:");
  scanf("%d", &valueLog);
  printf("%d에 자연로그를 곱하면 %f\n", valueLog, valueLog*LOGARITHM);

  // 7. 루트 2값 변환하기
  int valueRoot;
  printf("7.루트 2에 곱할 정수를 입력하세요 :");
  scanf("%d", &valueRoot);
  printf("%d에 루트 2를 곱하면 %f가 됩니다.\n", valueRoot, ROOT2 * valueRoot);

  // 8. 평당 단위 면접 m^2로 변환하기
  int size;
  printf("8. 몇 평인가요?: ");
  scanf("%d", &size);
  double totalSize = size * ROOM;
  printf("%d평은 %.2f제곱미터입니다.\n", size, totalSize);
  //
  // 9. 인치 -> cm 
  double valueCm;
  printf("9. 몇 인치를 cm단위로 환산하려고 하십니까?");
  scanf("%lf", &valueCm);
  printf("%f인치는 %fcm입니다.\n", valueCm, valueCm * INCH_TO_CM);
  //
  // 10. 포도개당 칼로리
  int numberGrape;
  printf("10. 먹은 포도 개수를 알려주세요: ");
  scanf("%d", &numberGrape);
  float calories = numberGrape * GRAPE_CALORIE;
  printf("총 칼로리는: %.2f\n", calories);
  return 0;
}
