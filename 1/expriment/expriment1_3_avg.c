#include <stdio.h>
#include <unistd.h>
int main()
{
    float m, n, l;
    printf("pid %d请输入要求平均值的3个数：", _getpid()); 
    scanf("%f%f%f", &m, &n, &l);
    printf("%f", (m + n + l) / 3);
}
