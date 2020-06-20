#include<stdio.h>
#include<unistd.h>
int main()
{
	pid_t pid = fork();
	if(pid < 0){
		printf("error!!");
	} else if(pid == 0){
		printf("子进程空间");
		exit(0);
	} else{
		printf("父进程空间，子进程程序号为%d\n", pid);
	}
	exit(0);
}
