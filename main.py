from datetime import date
import os
import zipfile

hoje = date.today()
dia = hoje.strftime("%d-%m-%Y")
pasta = f'E:/UNILAB/{dia}'

print(dia)

os.chdir(pasta)


zip = zipfile.ZipFile(f'{dia}.zip', 'w')

zip.write('*.txt')
zip.close()


print(os.listdir(pasta))