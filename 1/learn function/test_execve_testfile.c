#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
extern char **environ;
int main(int argc, char *argv[])
{
    int i = 0;
    //打印envp，新环境变量
    for( i = 0; environ[i] != NULL; i++ )
    {
        printf("environ[%d]:%s\r\n",i,environ[i]);
    }
 
    printf("\r\n\r\n");
 
    //打印argv，参数
    for( i = 0; i < argc; i++ )
    {
        printf("argv[%d]:%s\r\n",i,argv[i]);
    }
    return 0;
}
