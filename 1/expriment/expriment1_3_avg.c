#include <stdio.h>
#include <unistd.h>
int main()
{
    float m, n, l;
    printf("pid %d������Ҫ��ƽ��ֵ��3������", _getpid()); 
    scanf("%f%f%f", &m, &n, &l);
    printf("%f", (m + n + l) / 3);
}
