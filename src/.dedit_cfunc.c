#include<stdio.h>
#define MIN 1
#define MAX 25
int main()
{
	int x,n, value1;
	char orbital_symbol[]="spdfghijklmnopqrstuvwxyz";
	printf("주 양자 수를 입력하시오.\n*범위 : 1-25까지*\n");
	scanf("%d", &x);
	char *orbital_pointer[x];
	if(MIN<=x & x<=MAX)
	{

	int l[x];
	for(n=0;n<x;n++)
	{
		l[n]=n;
		if(n==x-1)
		{
			value1=l[n];
		}
		printf("오비탈 : %d%c\n", x, orbital_symbol[n]);
	}
	for(n=0;n<x;n++)
	{
	printf("방위 양자수 : %d\n", l[n]);
	}
for(n=-1*value1;n<=value1;n++)
{
	printf("자기 양자수 : %d\n", n);
}
printf("오비탈 수 : %d\n", x*x);
printf("최대 수용 전자 수 : %d\n", 2*x*x);
}
return 0;
}
