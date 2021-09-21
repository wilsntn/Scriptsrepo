import shutil
import os
from datetime import date

hoje = date.today()
dia = hoje.strftime("%d-%m-%Y")
pasta = f'E:/UNILAB/{dia}'
dst = 'E:/zipado'
files = os.listdir(pasta)
filesdst = os.listdir(dst)

os.chdir(pasta)

shutil.copy(pasta, dst)

