from pathlib import Path
from os import system

# base= Path.home()
# guia = Path(base,"Barcelona", "SagradraFamilia.txt")
# guia2=guia.with_name("La_pedrera.txt")
# print(base)
# print(guia)
# print(guia2)
# #Para obtener la carpeta parent anterior
# print

guia = Path(Path.home(),'Desktop','PythonProjects','pythonlearn','Path',"Europa")

for txt in Path(guia).glob("**/*.txt"):
    print(txt)

  
system('cls')