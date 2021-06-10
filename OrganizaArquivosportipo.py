import os
import getpass as gt
import shutil as sh

texto = ['.txt', '.docx', '.odt']
musica = ['.mp3', '.wav']
video = ['.mp4', '.3gp', '.mkv']
py = ['.ipynb', '.py']
pdf = '.pdf'
imagem = ['.jpeg', '.png', '.jpg', '.gif', ]
compact = ['.tar', '.zip', '.rar', '.xz', '.gz', '.deb']

Txt = f'/home/{gt.getuser()}/Documentos/Txts'
Jupyter = f'/home/{gt.getuser()}/Documentos/Script'
Outros = f'/home/{gt.getuser()}/Documentos/Outros'
Video = f'/home/{gt.getuser()}/Documentos/Videos'
Musica = f'/home/{gt.getuser()}/Documentos/Musicas'
Pdf = f'/home/{gt.getuser()}/Documentos/Pdfs'
Imagem = f'/home/{gt.getuser()}/Documentos/Imagens'
Compactad = f'/home/{gt.getuser()}/Documentos/Compactados'


def pesqarq(arquivo):
    os.chdir(arquivo)
    listarq = os.listdir(arquivo)
    extensoes = []
    for file in listarq:
        if os.path.isfile(file) == True:
            extensoes.append(file)
    return extensoes

def separa_arq(arquivo):
    os.chdir(arquivo)
    for tipo in pesqarq(arquivo):
        indice = tipo.rfind('.')
        final = tipo[indice:]
        final = final.lower()
        if final in texto:
            if os.path.isdir(Txt) == False:
                os.mkdir(Txt)
            if os.path.isfile(f'{Txt}/{tipo}') == False:
                sh.move(tipo, Txt)
            elif os.path.isfile(f'{Txt}/{tipo[:indice]}-1{final}') == False:
                sh.move(tipo, f'{Txt}/{tipo[:indice]}-1{final}')
            elif os.path.isfile(f'{Txt}/{tipo[:indice]}-2{final}') == False:
                sh.move(tipo, f'{Txt}/{tipo[:indice]}-2{final}')

        elif final in py:
            if os.path.isdir(Jupyter) == False:
                os.mkdir(Jupyter)
            if os.path.isfile(f'{Jupyter}/{tipo}') == False:
                sh.move(tipo, Jupyter)
            elif os.path.isfile(f'{Jupyter}/{tipo[:indice]}-1{final}') == False:
                sh.move(tipo, f'{Jupyter}/{tipo[:indice]}-1{final}')
            elif os.path.isfile(f'{Jupyter}/{tipo[:indice]}-2{final}') == False:
                sh.move(tipo, f'{Jupyter}/{tipo[:indice]}-2{final}')

        elif final in pdf:
            if os.path.isdir(Pdf) == False:
                os.mkdir(Pdf)
            if os.path.isfile(f'{Pdf}/{tipo}') == False:
                sh.move(tipo, Pdf)
            elif os.path.isfile(f'{Pdf}/{tipo[:indice]}-1{final}') == False:
                sh.move(tipo, f'{Pdf}/{tipo[:indice]}-1{final}')
            elif os.path.isfile(f'{Pdf}/{tipo[:indice]}-2{final}') == False:
                sh.move(tipo, f'{Pdf}/{tipo[:indice]}-2{final}')

        elif final in video:
            if os.path.isdir(Video) == False:
                os.mkdir(Video)
            if os.path.isfile(f'{Video}/{tipo}') == False:
                sh.move(tipo, Video)
            elif os.path.isfile(f'{Video}/{tipo[:indice]}-1{final}') == False:
                sh.move(tipo, f'{Video}/{tipo[:indice]}-1{final}')
            elif os.path.isfile(f'{Video}/{tipo[:indice]}-2{final}') == False:
                sh.move(tipo, f'{Video}/{tipo[:indice]}-2{final}')

        elif final in musica:
            if os.path.isdir(Musica) == False:
                os.mkdir(Musica)
            if os.path.isfile(f'{Musica}/{tipo}') == False:
                sh.move(tipo,Musica)
            elif os.path.isfile(f'{Musica}/{tipo[:indice]}-1{final}') == False:
                sh.move(tipo, f'{Musica}/{tipo[:indice]}-1{final}')
            elif os.path.isfile(f'{Musica}/{tipo[:indice]}-2{final}') == False:
                sh.move(tipo, f'{Musica}/{tipo[:indice]}-2{final}')

        elif final in imagem:
            if os.path.isdir(Imagem) == False:
                os.mkdir(Imagem)
            if os.path.isfile(f'{Imagem}/{tipo}') == False:
                sh.move(tipo,Imagem)
            elif os.path.isfile(f'{Imagem}/{tipo[:indice]}-1{final}') == False:
                sh.move(tipo, f'{Imagem}/{tipo[:indice]}-1{final}')
            elif os.path.isfile(f'{Imagem}/{tipo[:indice]}-2{final}') == False:
                sh.move(tipo, f'{Imagem}/{tipo[:indice]}-2{final}')

        elif final in compact:
            if os.path.isdir(Compactad) == False:
                os.mkdir(Compactad)
            if os.path.isfile(f'{Compactad}/{tipo}') == False:
                sh.move(tipo,Compactad)
            elif os.path.isfile(f'{Compactad}/{tipo[:indice]}-1{final}') == False:
                sh.move(tipo, f'{Compactad}/{tipo[:indice]}-1{final}')
            elif os.path.isfile(f'{Compactad}/{tipo[:indice]}-2{final}') == False:
                sh.move(tipo, f'{Compactad}/{tipo[:indice]}-2{final}')

        else:
            if os.path.isdir(Outros) == False:
                os.mkdir(Outros)
            if os.path.isfile(f'{Outros}/{tipo}') == False:
                sh.move(tipo, Outros)
            elif os.path.isfile(f'{Outros}/{tipo[:indice]}-1{final}') == False:
                sh.move(tipo, f'{Outros}/{tipo[:indice]}-1{final}')
            elif os.path.isfile(f'{Outros}/{tipo[:indice]}-2{final}') == False:
                sh.move(tipo, f'{Outros}/{tipo[:indice]}-2{final}')

arquivo=f'/home/{gt.getuser()}/Downloads'
tamanho = len(pesqarq(arquivo))
if tamanho !=0:
    separa_arq(arquivo)
    print(f'Foram movidos um total de {tamanho} arquivos')
    print(f'Movidos com sucesso para a pasta /home/{gt.getuser()}/Documentos/')
else:
    print('Nada a Mover')
