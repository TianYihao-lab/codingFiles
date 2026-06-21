#include <stdio.h>
#include <stdlib.h>


void test01(){
    char a='A';
    char m=65; // 等同于 char a = 'A';
    printf("%c\n",a); // 输出 A
    printf("%d\n",a);
    printf("%d\n",m);

    char b = 'B'; // 等同于 char a = 66;
    char c = 'C'; // 等同于 char b = 67;

    printf("%d\n", a + b); // 输出 133  
    printf("%c\n", a + b);  // 输出  (ASCII码的范围是0-127，超过127会变成不可见字符)

}

void test02(){
    char ch=getchar(); // ch=getche()

    while (getchar() != '\n');

    // gets函数 用来读取一个字符串
    char str[100];
    gets(str);
    // 使用gets()函数可以读取带有空格的字符串

    printf("你输入的字符是：%c\n", ch);
    putchar(ch); // putchar()函数用来输出一个字符
    printf("你输入的字符串是：%s\n", str);
    puts(str); // puts()函数用来输出一个字符串，并在字符串末尾自动添加换行符
    
}

int main(){
    test02();
    return 0;
}