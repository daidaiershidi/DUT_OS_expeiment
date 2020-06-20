#include <unistd.h>
#include <stdlib.h>
int main()
{
	pid_t pc,pr;
	pc=fork();
	if(pc<0) /* ������� */
		printf("error ocurred!/n");
	else if(pc==0){ /* ������ӽ��� */
		printf("This is child process with pid of %d\n",getpid());
		sleep(10); /* ˯��10���� */
	}
	else{ /* ����Ǹ����� */
		pr=wait(NULL); /* ������ȴ� */
		printf("I catched a child process with pid of %d\n",pr);
	}
	exit(0);
}
