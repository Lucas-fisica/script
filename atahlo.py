import os
import shutil as sh
import getpass as gt
import wget as wg
import zipfile as zp
import stat as st

local = os.listdir(f'/home/{gt.getuser()}')
caminho = f'/home/{gt.getuser()}/.local/share/applications' 
if '.local' not in local:
    os.makedirs(caminho)

os.chdir(caminho)

cmd = f'[Desktop Entry]\nEncoding=UTF-8\nVersion=1.0\nType=Application\n\
Exec=java -jar {caminho}/TLauncher-2.831.jar\n\
Icon={caminho}/image.png\n\
Name=Minecraft\nComment=Um Launcher de Minecraft'

with open('Minecraft.desktop', 'w') as  f:
    f.writelines(cmd)

os.chmod('Minecraft.desktop' , st.S_IRWXU)

print('Baixando o TLauncher')
url = ['https://raw.githubusercontent.com/Lucas-fisica/bagunca_arq/main/image.png','https://raw.githubusercontent.com/Lucas-fisica/bagunca_arq/main/TLauncher-2.831.zip']

for i in url:
    wg.download(i)
    print('\nfoi')
    
with zp.ZipFile('TLauncher-2.831.zip', 'r') as r:
    r.extract('TLauncher-2.831.jar')

os.remove('TLauncher-2.831.zip')
