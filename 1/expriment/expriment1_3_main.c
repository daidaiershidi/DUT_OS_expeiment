#include<unistd.h>
#include<string.h> 
#include<sys/wait.h>
#define N 10
main()
{
	char function_name[N];
	char *argv_send[] = {NULL};
	char *envp[] = {NULL};
	
	printf("pid %d(max,min,avg):", _getpid());
	scanf("%s", function_name);
	if(strcmp(function_name, "min") == 0){
		execl("./expriment1_3_min", NULL);
	} else if(strcmp(function_name, "max") == 0){
		execve("./expriment1_3_max", argv_send, envp);
	} else if(strcmp(function_name, "avg") == 0){
		execve("./expriment1_3_avg", argv_send, envp);
	} 
}
