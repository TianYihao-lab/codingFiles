#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>    // 包含stdbool.h头文件以使用bool类型


int main(){
    bool a = true; // bool类型只能存储true和false，true表示真，false表示假
    printf("%d\n", a); // 输出 1
    bool b = false; // bool类型只能存储true和false，true表示真，false表示假
    printf("%d\n", b); // 输出 0
    _Bool c = 1; // _Bool类型只能存储0和1，0表示假，1表示真
    printf("%d\n", c); // 输出 1

    return 0;
}