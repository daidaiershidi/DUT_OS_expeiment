#include<unistd.h>
main()
{

    char *envp[] = {NULL};
    char *argv_send[] = {NULL};
    int a = execve("./test_execve_testfile",argv_send,envp);

	printf("%d", a);
    return 0;
}
