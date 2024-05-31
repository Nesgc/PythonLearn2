from pathlib import Path
import os

rutabase=os.path.abspath(os.getcwd())
print('Bienvenido usuario, la ruta de acceso al directorio se encuentra en: ')
print(Path(rutabase,'Recetas'))
# base= Path.home()
# guia = Path(base,"Barcelona", "SagradraFamilia.txt")
# guia2=guia.with_name("La_pedrera.txt")
# print(base)
# print(guia)
# print(guia2)
# #Para obtener la carpeta parent anterior
# print

# guia = Path(Path.home(),'Desktop','PythonProjects','pythonlearn','Path',"Europa")

# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)

  
# system('cls')

# def abrir_leer(ruta_archivo):
#     with open(ruta_archivo, 'r') as archivo:
#         le=archivo.read()
#         return(le)
       