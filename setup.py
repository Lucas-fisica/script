import platform as pt
import os
import tarfile as tar
import shutil as sh
from urllib import error
import getpass as gt

urls = ['https://github.com/subhra74/xdm/releases/download/7.2.11/xdm-setup-7.2.11.tar.xz',
        'https://download-cdn.jetbrains.com/python/pycharm-community-2021.3.tar.gz']

prog = 'python-pip okular telegram-desktop vivaldi gimp bleachbit obs-studio'
sos = ''.join([i for i in pt.release().lower() if str.isalpha(i)])

if 'manjaro' in sos:
    os.system(f'sudo -S pamac update && sudo -S pamac install {prog} --no-confirm && '+
    f'sudo -S pamac build jdk --no-confirm')

else:
    os.system(f'sudo apt install {prog} -y')
print('terminado'.upper())

try:
    import wget as wg
except:
    os.system('pip install wget')
    import wget as wg

caminho = '/tmp/arq'
try:
    os.chdir(caminho)
except:
    os.mkdir(caminho)
    os.chdir(caminho)

for i in urls:
    print(i)
    try:
        if i==urls[0]:
            file = wg.download(i)

        else:
            file = wg.download(i)

    except error.HTTPError:
        continue

    pasta = f'{caminho}/{file[0:3]}'
    with tar.TarFile.open(file) as f:
        f.extractall(pasta)

    pastaf = f'/home/{gt.getuser()}/.local/programas'
    try:
        sh.move(pasta, pastaf)
    except:
        os.makedirs(pastaf)
        sh.move(pasta, pastaf)

print('terminado'.upper())
import stat as st

desk = f'[Desktop Entry]\n\
Exec=/home/{gt.getuser()}/.local/programas/pyc/pycharm-community-2021.3/bin/pycharm.sh\n\
Icon=/home/{gt.getuser()}/.local/programas/pyc/pycharm-community-2021.3/bin/pycharm.png\n\
Name=Pycharm'

pastadesk = f'/home/{gt.getuser()}/.local/share/applications'
with open(f'{pastadesk}/pycharmt.desktop', 'w') as f:
    f.writelines(desk)

os.chmod(f'{pastadesk}/pycharmt.desktop', st.S_IRWXU)
print('terminado'.upper())
