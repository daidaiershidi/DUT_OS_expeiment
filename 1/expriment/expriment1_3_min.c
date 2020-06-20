#include <stdio.h>
#include <unistd.h>
int main()
{
    float m,n;
    printf("pid %d请输入要求最小值的2个数：", _getpid()); 
    scanf("%f%f", &m, &n);
    
	if(m > n)
		printf("%f", n);
	else if(m < n) 
		printf("%f", m);
	else
		printf("一样大");
}
