#include<stdio.h>
#include<unistd.h>
int main()
{
	pid_t pid1, pid2;
	pid1 = fork(); // <--第一次fork 
	if(pid1 < 0){
		printf("error!!");
	} else if(pid1 == 0){
		pid2 = fork(); // <--第二次fork  
		if(pid2 < 0){
			printf("error!!");
		} else if(pid2 == 0){
			printf("\n子进程2pid为%d,子进程2无子进程pid\n", _getpid());
		} else{
			printf("子进程1pid为%d,子进程1的子进程pid为%d\n", _getpid(), pid2);
		} 
		
	} else{
		printf("父进程pid为%d,父进程的子进程pid为%d\n", _getpid(), pid1);
	}
	exit(0);
}
