#include <stdio.h>
#define include Blue-Encrypt.h
/*
 * Include criada por SrBlue.
 *
 * Copie este codigo e salve como Blue-Encrypt.h
 *
 * Use Encrypt(string);   Para Criptografada
 * Use UnEncrypt(string); Para Des-Criptografada
 *
 * exemplo: char string[100] = "paulo torrens lindo";
 *
 * Encrypt(string); // Criptrografar a string
 * printf("%s",string); // mostrar a string criptografada
 *
 * UnEncrypt(string); // Des Criptrografar a string
 * printf("%s",string); // mostrar string Des-Criptografada
 */
 
void Encrypt(char cla[5000])
{
	for(int i = 0; (i < 100 && cla[i] != '\0'); i++)
    cla[i] = cla[i] + 999;
}

void UnEncrypt(char cla[5000])
{
	for(int i = 0; (i < 100 && cla[i] != '\0'); i++)
    cla[i] = cla[i] - 999;
}
