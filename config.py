import os

import shutil as sh
import getpass as gt
import subprocess as sp

che = os.listdir('/bin')
if 'pip' in che:
    sp.check_output(['pip', 'install', '-U', 'pip'])
    sp.check_output(['pip', 'install', 'wget'])

else:
    sp.check_output(['echo', '"lu"', '|','sudo', '-S', 'pamac', 'install', 'python-pip'])
    sp.check_output(['pip', 'install', '-U', 'pip'])
    sp.check_output(['pip', 'install', 'wget'])

import wget as wg

urls = ['https://raw.githubusercontent.com/Lucas-fisica/bagunca_arq/main/OptiFine_1.18_HD_U_H3.jar',
       'https://raw.githubusercontent.com/Lucas-fisica/bagunca_arq/main/journeymap-1.18-5.8.0alpha9.jar']

print('baixando mods')
for i in urls:
    wg.download(i)
    print('baixou')

file = os.listdir('.')

destino = f'/home/{gt.getuser()}/.minecraft/mods/'
print('confdigurando o minecraft')
for e in file:
    if e[-4:] == '.jar':
        sh.move(e, destino)

print('ei'+'iiiiiii'*100)

