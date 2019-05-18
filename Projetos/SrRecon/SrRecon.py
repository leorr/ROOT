
import socket
import sys
import os
import requests
import OpenSSL
import ssl
import signal

info_string = \
r"""
   ██████  ██▀███        ██▀███  ▓█████ ▄████▄  ▒█████   ███▄    █ 
 ▒██    ▒ ▓██ ▒ ██▒     ▓██ ▒ ██▒▓█   ▀▒██▀ ▀█ ▒██▒  ██▒ ██ ▀█   █ 
 ░ ▓██▄   ▓██ ░▄█ ▒     ▓██ ░▄█ ▒▒███  ▒▓█    ▄▒██░  ██▒▓██  ▀█ ██▒ 1.0 DEMO
   ▒   ██▒▒██▀▀█▄       ▒██▀▀█▄  ▒▓█  ▄▒▓▓▄ ▄██▒██   ██░▓██▒  ▐▌██▒
 ▒██████▒▒░██▓ ▒██▒     ░██▓ ▒██▒░▒████▒ ▓███▀ ░ ████▓▒░▒██░   ▓██░
 ▒ ▒▓▒ ▒ ░░ ▒▓ ░▒▓░     ░ ▒▓ ░▒▓░░░ ▒░ ░ ░▒ ▒  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ░▒  ░ ░  ░▒ ░ ▒░       ░▒ ░ ▒░ ░ ░  ░ ░  ▒    ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░  ░  ░    ░░   ░        ░░   ░    ░  ░       ░ ░ ░ ▒     ░   ░ ░ 
       ░     ░             ░        ░  ░ ░         ░ ░           ░ 
                                      ░                                                          
 Desevolvido por SrBlue.
 Publicada no 5ubTools
 Eficiencia de 80% e diversão de 100% 
"""


print(info_string)



def IpPublico(andress): 
        
        #Essa função verifica se o ip é publico ou privado.
        #IpPublico("192.168.0.1")
        #return: False
        
        if re.match(r'^(?:10)(?:\.\d+){3}|(?:172\.(?:[1]:?[0-9]|[2]:?[0-9]|[3]:?[0-1]))(?:\.\d+){2}|(?:192.168)(?:\.\d+){2}|(?:127)(?:\.\d+){3}$', andress):
            return False
        return True
        
if len(sys.argv) < 2:
        print("[?] Use: ipRecon.py [IP/URL]")
        sys.exit()

host = sys.argv[1]
try:
        ip = socket.gethostbyname(host)
except:
        print("FALHA AO PEGAR HOST")
        print("TENTE TIRAR O HTTPS/HTTP")
        sys.exit()


print(" ")

try:
        print("HOST: %s"%host)
except:
        print("HOST: ERRO")

try:
        servidor = socket.gethostbyaddr(ip)
        print("SERVIDOR-DNS: %s"%(servidor[0]))
except:
        print("SERVIDOR-DNS: ERRO ")

try:
        public = IpPublico(ip)
        print("TIPO DE SERVIDOR: PUBLICO")
except:
        print("TIPO DE SERVIDOR: PRIVADO")
       

try:
        print("IP: %s"%(ip))
except:        
        print("IP: ERRO ")

sock = socket.socket()
SSL = "http://"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(2.5)
try:
	response = client.connect_ex((ip, 443))
	if response == 0:
		print("SSL: SIM")
		SSL = "https://"
		sock.connect((host,443))
		sslsock = ssl.wrap_socket(sock)
		cert_der = sslsock.getpeercert(True)
		# load binary certificate and get signature hash algorithm
		cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert_der)
		print ("Criptrografia SSL: %s"%(cert.get_signature_algorithm()))
except:
    	print("SSL: ERROR")
    	SSL = "http://"


headers = requests.get(SSL+host).headers

print("Linguagem: %s "%(headers["content-type"]))
try:
	print("Servidor: %s "%(headers["server"]))
except:
	print("Servidor: ERROR")

# CMS:
# 1 = Wordpress
# 2 = Joomla
# 3 = Mambo
# 4 = Drupal
# 5 = Magento
# 6 = Jekyll

CmsDetectar = [0,1,2,3,4,5,6] #detector de CMS by SrBlue


CmsDetectar[0] = 0
CmsDetectar[1] = 0
CmsDetectar[2] = 0
CmsDetectar[3] = 0
CmsDetectar[4] = 0
CmsDetectar[5] = 0
CmsDetectar[6] = 0


# Como adicionar um diretorio?

# url = requests.get(SSL+host+"/diretorio/") #/diretorio/ é pra botar o diretorio que o arquivo do CMS esta. 
# if not url.status_code == 404:  # Se esta com pagina nao esta erro
#       CmsDetectar[1] = 1                   # CmsDetectar[CMS] = Sim ou Nao ( 1 = sim | 2 = nao)

try: #tentando a conexao com o servidor.

        url = requests.get(SSL+host+"/wp-content/") #Cms WordPress .
        if not url.status_code == 404: 
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-admin/") #Cms WordPress .
        if not url.status_code == 404: 
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-login.php") #Cms WordPress .
        if not url.status_code == 404: 
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-includes") #Cms WordPress .
        if not url.status_code == 404: 
                CmsDetectar[1] = 1
                

        url = requests.get(SSL+host+"/wp-config.php") #Cms WordPress .
        if not url.status_code == 404: 
                CmsDetectar[1] = 1
                

        ############
        ############       

        url = requests.get(SSL+host+"/joomla/")

        url = requests.get(SSL+host+"/javascript/") #Cms Joomla .
        if not url.status_code == 404: 
                CmsDetectar[2] = 1
                
                                
        url = requests.get(SSL+host+"/language/") #Cms Joomla .
        if not url.status_code == 404: 
                CmsDetectar[2] = 1
                
                                
        url = requests.get(SSL+host+"/Template_preview.png/") #Cms Joomla .
        if not url.status_code == 404: 
                CmsDetectar[2] = 1
                
                
        url = requests.get(SSL+host+"/template_thumbnail.png/") #Cms Joomla .
        if not url.status_code == 404: 
                CmsDetectar[2] = 1
                
                        
        url = requests.get(SSL+host+"/error.php/") #Cms Joomla .
        if not url.status_code == 404: 
                CmsDetectar[2] = 1
                
        ############
        ############
        url = requests.get(SSL+host+"/administrator/backups/") #Cms Mambo .
        if not url.status_code == 404: 
                CmsDetectar[3] = 1
                
                
        url = requests.get(SSL+host+"/administrator/") #Cms Mambo .
        if not url.status_code == 404: 
                CmsDetectar[3] = 1
                
                
                                
        url = requests.get(SSL+host+"/mambots/") #Cms Mambo .
        if not url.status_code == 404: 
                CmsDetectar[3] = 1
                
        ############
        ############
                                        
        url = requests.get(SSL+host+"/sites/all/") #Cms Drupal .
        if not url.status_code == 404: 
                CmsDetectar[4] = 1
                
                                                
        url = requests.get(SSL+host+"/sites/all/libraries/") #Cms Drupal .
        if not url.status_code == 404: 
                CmsDetectar[4] = 1
                
                                                        
        url = requests.get(SSL+host+"/sites/all/themes/") #Cms Drupal .
        if not url.status_code == 404: 
                CmsDetectar[4] = 1
                
                                                        
        url = requests.get(SSL+host+"/sites/all/modules/custom/") #Cms Drupal .
        if not url.status_code == 404: 
                CmsDetectar[4] = 1
                
                                                        
        url = requests.get(SSL+host+"/site/all/modules/contrib") #Cms Drupal .
        if not url.status_code == 404: 
                CmsDetectar[4] = 1
                
        ############
        ############
        url = requests.get(SSL+host+"/app/code/") #Cms Magento .
        if not url.status_code == 404: 
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/app/design/") #Cms Magento .
        if not url.status_code == 404: 
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/app/etc/") #Cms Magento .
        if not url.status_code == 404: 
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/downloader/") #Cms Magento .
        if not url.status_code == 404: 
                CmsDetectar[5] = 1
                

        url = requests.get(SSL+host+"/app/") #Cms Magento .
        if not url.status_code == 404: 
                CmsDetectar[5] = 1
                
        ############
        ############
        ############

        url = requests.get(SSL+host+"/jekyll/") #Cms Jekyll .
        if not url.status_code == 404: 
                CmsDetectar[6] = 1
                

        url = requests.get(SSL+host+"/_config.yml") #Cms Jekyll .
        if not url.status_code == 404: 
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/.jekyll-metadata") #Cms Jekyll .
        if not url.status_code == 404: 
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/_layouts") #Cms Jekyll .
        if not url.status_code == 404: 
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/404.md") #Cms Jekyll .
        if not url.status_code == 404: 
                CmsDetectar[6] = 1

        url = requests.get(SSL+host+"/about.md") #Cms Jekyll .
        if not url.status_code == 404: 
                CmsDetectar[6] = 1
                
                
                
except: #Se falhar a conexao com o servidor.
        print("FALHA AO CONECTAR A SERVIDOR HTTP/HTPPS")
        
        

# Definição dos CMS
# IF CmsDetectar[CMS] == 1: # Se a CMS for true 
# CMS  =  " NOME DA CMS "   # retorna CMS = "nome dela"


CMS = "ERROR"
if CmsDetectar[1] == 1:
        CMS = "Wordpress"
if CmsDetectar[2] == 1:
        CMS = "Joomla"
if CmsDetectar[3] == 1:
        CMS = "Mambo"
if CmsDetectar[4] == 1:
        CMS = "Drupal"
if CmsDetectar[5] == 1:
        CMS = "Magento"
if CmsDetectar[6] == 1:
        CMS = "Jekyll"

print("CMS: %s "%(CMS))

# 1 = Wordpress
# 2 = Joomla
# 3 = Mambo
# 4 = Drupal
# 5 = Magento
# 6 = Jekyll

print(" ")
print("Listando as Portas: ")



portas = [21,22,23,25,80,81,110,113,143,443,587,2525,3306,8080]
portasdebug = 1
for i in portas:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1.5)
    try:
        response = client.connect_ex((ip, i))
        if response == 0:
                print("PORTA: %s ABERTA"%(str(i)))
    except:
        portasdebug = 0

print(" ")
print("Localização da HOST: ")
url = "https://api.hackertarget.com/geoip/?q=" + host 
request = requests.get(url)
localizar = request.text
print(localizar)

        
