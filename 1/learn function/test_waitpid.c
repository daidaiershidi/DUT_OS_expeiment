#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>
int main()
{
	pid_t pc,pr;
	pc=fork();
	if(pc<0) /* 如果出错 */
		printf("error ocurred!/n");
	else if(pc==0){ /* 如果是子进程 */
		printf("This is child process with pid of %d\n",getpid());
		sleep(10); /* 睡眠10秒钟 */
	}
	else{ /* 如果是父进程 */
		while(pr == 0)
			pr=waitpid(pc, NULL, WNOHANG); /* 在这里等待 */
			printf("process id %d do not release \n", pc); /*并不会在上一行等待*/
		printf("I catched a child process with pid of %d\n",pr);
	}
	exit(0);
}
