#include<stdio.h>
#include<unistd.h>
int main()
{
	pid_t pid = fork();
	if(pid < 0){
		printf("error!!");
	} else if(pid == 0){
		printf("�ӽ��̿ռ�");
		exit(0);
	} else{
		printf("�����̿ռ䣬�ӽ��̳����Ϊ%d\n", pid);
	}
	exit(0);
}
