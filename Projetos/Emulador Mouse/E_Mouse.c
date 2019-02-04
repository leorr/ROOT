#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

//////////////////////////
/// Use as flecha do teclado para mover o mouse
/// Use o numero 1 para dar click esquerdo do mouse
/// Use o numero 2 para dar click direto do mouse
/// Use o DELETE para pausar o programa para fecha-l
/// Use PagUp Ou PagDown para aumentar e abaixar a sensibilidade das teclas.
/////////////////////////

// SetCursorPos(x,y) setar local do mouse;
// GetCursorPos(&variavel) coletar local do mouse;

void LeftClick ( )
{  
  INPUT    Input={0};
  // left down 
  Input.type      = INPUT_MOUSE;
  Input.mi.dwFlags  = MOUSEEVENTF_LEFTDOWN;
  ::SendInput(1,&Input,sizeof(INPUT));

  // left up
  ::ZeroMemory(&Input,sizeof(INPUT));
  Input.type      = INPUT_MOUSE;
  Input.mi.dwFlags  = MOUSEEVENTF_LEFTUP;
  ::SendInput(1,&Input,sizeof(INPUT));
}
void RightClick()
{
    INPUT Input = {0};
    // right down
    Input.type = INPUT_MOUSE;
    Input.mi.dwFlags = MOUSEEVENTF_RIGHTDOWN;
    ::SendInput(1,&Input,sizeof(INPUT));
    
	//right up
    ::ZeroMemory(&Input,sizeof(INPUT));
    Input.type = INPUT_MOUSE;
    Input.mi.dwFlags = MOUSEEVENTF_RIGHTUP;
    ::SendInput(1,&Input,sizeof(INPUT));
}
int sen;
int main(void)
{
	system("title Pegar Cordes");
	printf("Aperte Delete para sair do programa.");
	printf("RECOMENDO ( 1 - 50 )\n");
	printf("NAO ME RESPONSABILIZO POR NADA!\n");
	printf("Escolha a sensibilidade das tecla que voce queira: ");
	scanf("%d",&sen);
	POINT coods;
	for( ; ; ) 
	{
		GetCursorPos(&coods);
		system("cls");
		printf("%i, %i",coods.x,coods.y);
		printf("\nSensibilidade: %i",sen);
		printf("\n\nArrows do teclado para mover o mouse \nNumero 1 Botao esquerdo\nNumero 2 Botao direto\nDELETE para pausar o programa\nPagUp para aumentar sensibilidade\nPagDown pra abaixar sensibilidade.");
		if(GetAsyncKeyState(0x2E))
		{
			exit(0);
		}
			if(GetAsyncKeyState(VK_UP))
			{
				coods.y = coods.y - sen;
				SetCursorPos(coods.x,coods.y);	
			}
				if(GetAsyncKeyState(VK_DOWN))
				{
					coods.y = coods.y + sen;
					SetCursorPos(coods.x,coods.y);
				}
					if(GetAsyncKeyState(VK_LEFT))
					{
						coods.x = coods.x - sen;
						SetCursorPos(coods.x,coods.y);	
					}
						if(GetAsyncKeyState(VK_RIGHT))
						{
							coods.x = coods.x + sen;
							SetCursorPos(coods.x,coods.y);	
						}
							if(GetAsyncKeyState(0x31))
							{
								LeftClick();
							}
								if(GetAsyncKeyState(0x32))
								{
									RightClick();
						    	}
									if(GetAsyncKeyState(VK_PRIOR))
									{
										sen++;	
									}
										if(GetAsyncKeyState(VK_NEXT))
										{
											sen--;	
										}			
////__//__//__//__//__//___//__//__//__//								
	
	}
	return 1;
}
