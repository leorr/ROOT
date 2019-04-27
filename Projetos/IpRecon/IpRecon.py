#!/usr/bin/python
import socket
import requests
import sys
import os.path
#script Analise de site IP + CM.S + DNS + SC/AN P'ORTS


host = sys.argv[1]

# 0 = Wordpress
# 1 = Joomla
# 2 = Magento
# 3 = Drupal
# 4 = Phpmyadmin
achou = 0
CmsDetectar = [0,1,2,3,4] #detector de CMS by SrBlue
url = requests.get("http://"+host+"/wp-content/") #Cms WordPress .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[0] = 1
        achou = 1
else:
        CmsDetectar[0] = 2

        
url = requests.get("http://"+host+"/plugins/tags/wp-content/") #Cms WordPress .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[0] = 1
        achou = 1
else:
        CmsDetectar[0] = 2


url = requests.get("http://"+host+"/wp-login.php/") #Cms Wordpress .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[0] = 1
        achou = 1
else:
        CmsDetectar[0] = 2

url = requests.get("http://"+host+"/content/wp-admin/") #Cms Wordpress .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[0] = 1
        achou = 1
else:
        CmsDetectar[0] = 2


url = requests.get("http://"+host+"/administrator/") #Cms Joomla .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[1] = 1
        achou = 1
else:
        CmsDetectar[1] = 2

url = requests.get("http://"+host+"/css/") #Cms Joomla .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[1] = 1
        achou = 1
else:
        CmsDetectar[1] = 2

url = requests.get("http://"+host+"/html/") #Cms Joomla .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[1] = 1
        achou = 1
else:
        CmsDetectar[1] = 2

url = requests.get("http://"+host+"/images/") #Cms Joomla .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[1] = 1
        achou = 1
else:
        CmsDetectar[1] = 2

url = requests.get("http://"+host+"/javascript/") #Cms Joomla .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[1] = 1
        achou = 1
else:
        CmsDetectar[1] = 2
        
url = requests.get("http://"+host+"/component.php") #Cms Joomla .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[1] = 1
else:
        CmsDetectar[1] = 2

url = requests.get("http://"+host+"/error.php") #Cms Joomla .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[1] = 1
        achou = 1
else:
        CmsDetectar[1] = 2

url = requests.get("http://"+host+"/skin/frontend/default/default/css/") #Cms Magento .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[2] = 1
        achou = 1
else:
        CmsDetectar[2] = 2

url = requests.get("http://"+host+"/errors/design.xml") #Cms Magento .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[2] = 1
        achou = 1
else:
        CmsDetectar[2] = 2

url = requests.get("http://"+host+"/js/mage/cookies.js") #Cms Magento .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[2] = 1
        achou = 1
else:
        CmsDetectar[2] = 2

url = requests.get("http://"+host+"/skin/frontend/default/default/css/") #Cms Magento .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[2] = 1
        achou = 1
else:
        CmsDetectar[2] = 2

url = requests.get("http://"+host+"/core/") #Cms Drupal .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[3] = 1
        achou = 1
else:
        CmsDetectar[3] = 2

url = requests.get("http://"+host+"/themes/") #Cms Drupal .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[3] = 1
        achou = 1
else:
        CmsDetectar[3] = 2

url = requests.get("http://"+host+"/sites/default/files/js/") #Cms Drupal .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[3] = 1
        achou = 1
else:
        CmsDetectar[3] = 2

url = requests.get("http://"+host+"/web.config") #Cms Drupal .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[3] = 1
        achou = 1
else:
        CmsDetectar[3] = 2
        
url = requests.get("http://"+host+"/modules/") #Cms Drupal .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[3] = 1
        achou = 1
else:
        CmsDetectar[3] = 2

url = requests.get("http://"+host+"/config.inc.php") #Cms Phpmyadmin .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[4] = 1
        achou = 1
else:
        CmsDetectar[4] = 2

url = requests.get("http://"+host+"/phpmyadmin/") #Cms Phpmyadmin .
if url.status_code == 200 and achou == 0: 
        CmsDetectar[4] = 1
        achou = 1
else:
        CmsDetectar[4] = 2
CMS = "ERROR"
if CmsDetectar[0] == 1:
        CMS = "Wordpress"
if CmsDetectar[1] == 1:
        CMS = "Joomla"
if CmsDetectar[2] == 1:
        CMS = "Magento"
if CmsDetectar[3] == 1:
        CMS = "Drupal"
if CmsDetectar[4] == 1:
        CMS = "PhpMyAdmin"
        
print("CMS: %s "%(CMS))
