import sys
import os
from cx_Freeze import setup,Executable

#Definir arquivos 
arquivos = [''] #adiciona os arquivos do projeto
#saida de arquivos
configuracao = Executable(
    script='', # nome do arquivo principal
    icon=''# nome do icone do projeto
)
#configuracao
setup(
    name='', # nome do projeto
    version='', #versao do projeto
    description='', # descricao do projeto
    author='', #autoro do projeto
    options={'build_exe':{
        'include_files': arquivos,
        'include_msvcr': True
    }},
    executables=[configuracao]
)