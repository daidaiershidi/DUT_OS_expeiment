#include<stdio.h>
#include<unistd.h>
int main()
{
	pid_t pid0, pid1, pid2;
	pid0 = _getpid();
	pid1 = fork(); // <--��һ��fork 
	if(pid1 < 0){
		printf("error!!");
	} else if(pid1 == 0){
		printf("�ӽ���1pidΪ%d\n", _getpid());
	} else{
		pid2 = fork(); // <--�ڶ���fork  
		if(pid2 < 0){
			printf("error!!");
		} else if(pid2 == 0){
			printf("�ӽ���2pidΪ%d\n", _getpid());
		} else{
			printf("������pidΪ%d,�����̵��ӽ���1pidΪ%d,�����̵��ӽ���2pidΪ%d\n", pid0, pid1, pid2);
		} 
	}
}
