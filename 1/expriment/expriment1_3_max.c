#include <stdio.h>
#include <unistd.h>
int main()
{
    float m,n;
    printf("pid %d������Ҫ�����ֵ��2������", _getpid()); 
    scanf("%f%f", &m, &n);
    
	if(m > n)
		printf("%f", m);
	else if(m < n) 
		printf("%f", n);
	else
		printf("һ����");
}
