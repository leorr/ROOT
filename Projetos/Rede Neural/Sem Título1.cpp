// DECLARAÇÃO DAS BIBLIOTECAS
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <windows.h>
#include <math.h>
#include <time.h>
#include <windows.h>
#include <conio.c>
// VARIAVEIS

int encina[5];
int ba;


// VOIDS

void teste();
void DesBug();
void sla();
void resetar();

// INTERFACE
int main (void) 
{
	SetConsoleTitle("IA");
	DesBug();
	return 1;
}

void DesBug()
{
	teste();
}

void sla()
{
	int op;
	textcolor(WHITE);
	printf("\n[++] Escolhendo vector\n");
	op =(rand() % 10) + 1;
	if(op >= 5)
	{
		op =(rand() % 10) + 1;
		if(op >= 5)
		{
			op =(rand() % 10) + 1;
		}
			if(op >= 5)
			{
				op =(rand() % 10) + 1;
				if(op >= 5)
				{
					op =(rand() % 10) + 1;
				}	
			}
	}	
	FILE * pFile;
  	pFile = fopen ("ia.txt","a");
  	if (pFile!=NULL)
  	{
		for (int i = 0; i < op; i++)
		{
		textcolor(YELLOW);
		printf("\n [%i] variavel %d vetor %i",i,encina[i],i);
		fprintf (pFile,"\n [%i] variavel %d vetor %i",i,encina[i],i);
		}	
	fclose(pFile);
	}
	resetar();
}

void resetar()
{
	for(int i= 0; i < 5; i++)
	{
		encina[i] = 0;
	}
	textcolor(WHITE);
	printf("\n[++] Todas variaveis foram resetadas!");
	Sleep(1500);
	system("cls");
	teste();
}

void teste()
{
	textcolor(WHITE);
	printf("\n[x] Apredendo... \n -> ");
	Sleep(2000);
	for (int i = 0; i < 5; i++)
	{
		if(encina[i] == 0)
		{
			int r;
			r = (rand() % 1400) + 1;
			encina[i]=r;
			textcolor(GREEN);
			printf("\nAprendi o numero %i do vector %i\n",encina[i], i);
		}
	}
	sla();
}
