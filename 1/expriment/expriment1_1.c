#include<stdio.h>
#include<unistd.h>
int main()
{
	pid_t pid1, pid2;
	pid1 = fork(); // <--��һ��fork 
	if(pid1 < 0){
		printf("error!!");
	} else if(pid1 == 0){
		pid2 = fork(); // <--�ڶ���fork  
		if(pid2 < 0){
			printf("error!!");
		} else if(pid2 == 0){
			printf("\n�ӽ���2pidΪ%d,�ӽ���2���ӽ���pid\n", _getpid());
		} else{
			printf("�ӽ���1pidΪ%d,�ӽ���1���ӽ���pidΪ%d\n", _getpid(), pid2);
		} 
		
	} else{
		printf("������pidΪ%d,�����̵��ӽ���pidΪ%d\n", _getpid(), pid1);
	}
	exit(0);
}
