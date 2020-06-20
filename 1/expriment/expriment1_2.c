#include<stdio.h>
#include<unistd.h>
int main()
{
	pid_t pid0, pid1, pid2;
	pid0 = _getpid();
	pid1 = fork(); // <--第一次fork 
	if(pid1 < 0){
		printf("error!!");
	} else if(pid1 == 0){
		printf("子进程1pid为%d\n", _getpid());
	} else{
		pid2 = fork(); // <--第二次fork  
		if(pid2 < 0){
			printf("error!!");
		} else if(pid2 == 0){
			printf("子进程2pid为%d\n", _getpid());
		} else{
			printf("父进程pid为%d,父进程的子进程1pid为%d,父进程的子进程2pid为%d\n", pid0, pid1, pid2);
		} 
	}
}
