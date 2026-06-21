#include <stdio.h>
#include <stdlib.h>

int a = 12;  // a是一个全局变量

int main(){
    if (a == 12) {
    int b = 99;
    printf("%d %d\n", a, b);  // 12 99
}

    printf("%d\n", a);  // 12
    // printf("%d\n", b);  // 出错
    {
        a=24;
        printf("%d\n",a);  // 24
    }
    return 0; 
}
