## Mac OS에서 C 프로그램 실행 방법
```
$ gcc filename.c -o filename
$ ./filename
```

## Variables and Types

### Data Types

* Integers: 
  - Whole numbers which can be either or negative. 
  - Defined using `char`, `int`, `short`, `long`, `long long`.

* Unsigned integers:
  - Whole numbers which can only be positive. 
  - Defined using `unsigned char`, `unsigned int`, `unsigned short`, `unsigned long`, `unsigned long long`.

* Floating point numbers
  - Real numbers (numbers with fractions).
  - Defined using `float` and `double`.

* Structures
  - TODO: 배워서 채워넣기

* Boolean 타입 따로 없으니 TRUE 1, FALSE 0으로 정의해서 쓸 것

## Arrays

- Array도 마찬가지로 정의하고 써야한다.
- Arrays can only have one type of variable, because they are implemented as a sequence of values in the computer's memory. Because of that, accessing a specific array cell is very efficient.

## Multidimensional Arrays

[출처](https://www.learn-c.org/en/Multidimensional_Arrays)
### Defining Example
- `type name[size1][size2]...[sizeN];`
- `int foo[1][2][3];`
- `char vowels[1][5] = {'a', 'e', 'i', 'o', 'u'`};`

### Initializing two-dimensional arrays

- Multidimensional arrays may be used by specifying bracketed[] values for each row.
- The inside braces, which indicates the wanted row, are optional. 행을 맞춰 쓰지 않아도 된다.

