from core.get_mail import *
import os
try:
   os.remove("index.html")
except:
    pass
print('''
 
 _____ ________  _________  ___  ___  ___  _____ _     
|_   _|  ___|  \/  || ___ \ |  \/  | / _ \|_   _| |    
  | | | |__ | .  . || |_/ / | .  . |/ /_\ \ | | | |    
  | | |  __|| |\/| ||  __/  | |\/| ||  _  | | | | |    
  | | | |___| |  | || |     | |  | || | | |_| |_| |____
  \_/ \____/\_|  |_/\_|     \_|  |_/\_| |_/\___/\_____/
                                                       
                                                       
                               
 Author : Asim
 Facebook : Ⱥsim Xhakma
''')
print("Staring Php Server")
os.system("php -S localhost:8000  > /dev/null 2>&1 &")
print("Server is running at http://localhost:8000/")
get_email_response()