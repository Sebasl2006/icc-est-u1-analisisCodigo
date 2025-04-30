
class metodosOrdenamiento:
    
    def sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)

        for i in range (n):
            for j in range (i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo [i]

        return arreglo
    

    def sort_bubble_mejorado(self, array):
        n = len(array)
        for i in range (n -1):
            cambio = False
            for j in range( n - i - 1):
                 if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo [i]
                    cambio = True
            if cambio == False:
                break


    def sort_seleccion(self, array):
        n = len(array)
        for i in range (n - 1):
            aux = array[i]
            for j in range (i + 1 , n):


