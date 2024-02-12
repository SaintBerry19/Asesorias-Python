class TercerElemento:
    def __init__(self, lista):
        self.lista = lista

    def obtener_tercer_elemento(self):
        if len(self.lista) >= 3:
            return self.lista[2]
        else:
            return None

    def es_el_tercer_elemento_el_mayor(self):
        tercer_elemento = self.obtener_tercer_elemento()
        if tercer_elemento is not None:
            if all(tercer_elemento >= elemento for elemento in self.lista):
                print("El tercer elemento es el más grande de la lista.")
            else:
                print("El tercer elemento no es el más grande de la lista.")
        else:
            print("La lista no tiene suficientes elementos para comparar.")

# Ejemplo de uso
lista = [1, 2, 5, 4, 3]
objeto = TercerElemento(lista)
print("Tercer elemento:", objeto.obtener_tercer_elemento())
objeto.es_el_tercer_elemento_el_mayor()

lista_corta = [1, 2]
objeto_corto = TercerElemento(lista_corta)
print("Tercer elemento en lista corta:", objeto_corto.obtener_tercer_elemento())
objeto_corto.es_el_tercer_elemento_el_mayor()
