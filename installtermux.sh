#!/data/data/com.termux/files/usr/bin/bash

clear
echo "====================================="
echo "   INSTALLTERMUX - DEPENDENCIAS"
echo "====================================="

sleep 1

echo "[*] Actualizando paquetes..."
pkg update -y && pkg upgrade -y

echo "[*] Instalando repositorios extra..."
pkg install -y root-repo
pkg install -y unstable-repo
pkg install -y x11-repo

echo "[*] Instalando dependencias base..."
pkg install -y git
pkg install -y wget
pkg install -y curl
pkg install -y unzip
pkg install -y zip
pkg install -y openjdk-17
pkg install -y python
pkg install -y python-pip
pkg install -y nodejs
pkg install -y clang
pkg install -y make
pkg install -y nano
pkg install -y vim
pkg install -y ruby
pkg install -y tsu

echo "[*] Instalando herramientas utiles..."
pkg install -y proot
pkg install -y tar
pkg install -y libxml2
pkg install -y libxslt
pkg install -y ncurses-utils

echo "[*] Instalando apktool..."
pkg install -y apktool

if ! command -v apktool &> /dev/null
then
    echo "[!] apktool no instalado, clonando alternativa..."
    git clone https://github.com/iBotPeaches/Apktool.git
fi

echo "[*] Instalando metasploit (msfvenom)..."
pkg install -y metasploit

if ! command -v msfvenom &> /dev/null
then
    echo "[!] metasploit fallo, intentando repo alternativo..."
    git clone https://github.com/gushmazuko/metasploit_in_termux.git
    cd metasploit_in_termux
    chmod +x metasploit.sh
    ./metasploit.sh
    cd ..
fi

echo "[*] Descargando uber-apk-signer..."
mkdir -p $HOME/tools
cd $HOME/tools

wget https://github.com/patrickfav/uber-apk-signer/releases/latest/download/uber-apk-signer.jar -O uber-apk-signer.jar

if [ ! -f "uber-apk-signer.jar" ]; then
    echo "[!] fallo descarga uber signer, intentando otra fuente..."
    curl -L -o uber-apk-signer.jar https://repo1.maven.org/maven2/com/github/patrickfav/uber-apk-signer/1.3.0/uber-apk-signer-1.3.0.jar
fi

cd $HOME

echo "[*] Instalando dependencias python..."
pip install --upgrade pip
pip install requests
pip install colorama
pip install flask
pip install bs4

echo "[*] Instalando dependencias ruby..."
gem install bundler

echo "[*] Configurando alias..."
echo "alias ubersigner='java -jar \$HOME/tools/uber-apk-signer.jar'" >> ~/.bashrc

echo "[*] Verificando instalaciones..."
echo "-------------------------------"

echo -n "apktool: "
command -v apktool && echo "OK" || echo "NO"

echo -n "msfvenom: "
command -v msfvenom && echo "OK" || echo "NO"

echo -n "java: "
command -v java && echo "OK" || echo "NO"

echo -n "git: "
command -v git && echo "OK" || echo "NO"

echo "-------------------------------"
echo "[✓] Instalacion terminada"
echo "Reinicia Termux para aplicar cambios"