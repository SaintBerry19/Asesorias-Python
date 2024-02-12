palabra='pendejo'
nueva_palabra=[]
for index,letter in enumerate(palabra):
    ansi_value = ord(letter)
    new_ansi_value = ansi_value + index
    nueva_letra = chr(new_ansi_value)
    nueva_palabra.append(nueva_letra)
nueva_palabra = "".join(nueva_palabra)
print(nueva_palabra)

nueva_palabra = ''.join(chr(ord(letter) + index) for index, letter in enumerate(palabra))
print(nueva_palabra)

base='abcdefghijklmnopqrstuvwxyz'
nueva_palabra=[]
for index,letter in enumerate(palabra):
    indice_letra=base.index(letter)
    nueva_letra=base[indice_letra + index]
    nueva_palabra.append(nueva_letra)  
nueva_palabra = "".join(nueva_palabra)
print(nueva_palabra)