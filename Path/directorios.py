from pathlib import Path
import os

rutabase=os.path.abspath(os.getcwd())
recetasfolder= Path(rutabase,'Path','Recetas')
print('Bienvenido usuario, la ruta de acceso al directorio se encuentra en: ')
print(recetasfolder)

print('Esta es la cantidad de recetas que tienes: ')
def recetastxt():
    # for txt in Path(recetasfolder).glob("**/*.txt"):
    #     print(txt)
    contador= 0
    for txt in Path(recetasfolder).glob("**/*.txt"):
        
        contador+=1
    print(contador)

recetastxt()

def optionone():
    recetascarnes= Path(os.path.abspath(os.getcwd()),'Path','Recetas','Carnes')

    category=input('Que categoria eliges? Carne, Ensaladas, Pastas, Postres:')
    if category == 'Carne':
        for txt in Path(recetascarnes).glob("**/*.txt"):
            print(txt.name)

        Recetacarneelegida = input('Elija una receta de carne: ')
        receta_path = recetascarnes / Recetacarneelegida
        if Recetacarneelegida == 'Entrecot al Malbec.txt':
            archivo=open(receta_path,'r')
            contenido=archivo.read()
            print(contenido)
    elif category == 'Ensaladas':
        print('elegiste 2')
    elif category == 'Pastas':
        print('elegiste 3')
    elif category == 'Postres':
        print('elegiste 4')
    else:
        print('Selecciona una opcion valida')
        optionone()

def choose():
    optionchosen=input('Elige una opcion 1,2,3 o 4')
    if optionchosen == '1':
        optionone()

    elif optionchosen == '2':
        print('elegiste 2')
    elif optionchosen == '3':
        print('elegiste 3')
    elif optionchosen == '4':
        print('elegiste 4')
    else:
        choose()

choose()


