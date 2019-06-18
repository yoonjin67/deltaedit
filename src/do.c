#include<stdio.h>
int main()
{
int x;
FILE *f=fopen("gcalc.py", "a+");
for(x=0;x<10;x++)
	fprintf(f,"	btn%d.connect('clicked',self.b1)\n",x);
for(x=0;x<10;x++)
	fprintf(f,"	def b%d:\n		self.entry.insert_text('%d')\n",x,x);
fclose(f);
return 0;
}
