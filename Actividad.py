import csv

archivo = open("C:\Users\Teo\Desktop\appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')

encabezado = next(csvreader)
print (encabezado)
for linea in csvreader:
    if linea[7] == '0' and 'ES' in linea[12] :
        print(linea,'\n')

archivo.close()
