#include <stdio.h>
#include <unistd.h>
int main()
{
    float m,n;
    printf("pid %d������Ҫ����Сֵ��2������", _getpid()); 
    scanf("%f%f", &m, &n);
    
	if(m > n)
		printf("%f", n);
	else if(m < n) 
		printf("%f", m);
	else
		printf("һ����");
}
