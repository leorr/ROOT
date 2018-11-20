#include <stdio.h>
#include <windows.h>
#include <cstdlib>
#include <stdlib.h>
#include <unistd.h>

#define CRACK 15

int seg = 0;
int min = 0;
int hor = 0;
int ml = 0;
int mls = 0;

void marcar();

int main()
{
	SetConsoleTitle("Cronometro");
	marcar();
	return 0;	
}

void marcar()
{
	for (;;)
	{
		mls++;
		usleep(0);
		system("cls");
		printf("%i:%i:%i:%i:%i",hor,min,seg,ml,mls);
		if(mls == CRACK)
		{
			ml++;
			mls = 0;
		}
		if(ml == 10)
		{
			seg++;
			ml = 0;
		}
		if(seg == 60)
		{
			min++;
			seg = 0;
		}
		if(min == 60)
		{
			hor++;
			min = 0;
		}
		if(hor == 24)
		{
			Sleep(5000);
			printf("Resetando...");
			hor = 0;
			min = 0;
			seg = 0;
		}
	}	
}


