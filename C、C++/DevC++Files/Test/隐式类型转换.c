#include <stdio.h>
#include <stdlib.h>

int main(){
    char x = 10;
    int y = x ;		// x和y所占用的内存空间大小不同，但是值相同。
    printf("%c\n", x); // 输出 10 和换行符
    printf("%d\n", y); // 输出 10 和换行符

    // 宽类型变成窄类型
    int i = 321;
    char ch = i; // ch 的值是 65 （321 % 256 的余值）,我们称这时候发生了截位。
    printf("%d\n", i); // 输出 321 和换行符
    printf("%c\n", ch); // 输出 65 和 'A'
    return 0;
}