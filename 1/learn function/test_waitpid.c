#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>
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
		while(pr == 0)
			pr=waitpid(pc, NULL, WNOHANG); /* ������ȴ� */
			printf("process id %d do not release \n", pc); /*����������һ�еȴ�*/
		printf("I catched a child process with pid of %d\n",pr);
	}
	exit(0);
}
