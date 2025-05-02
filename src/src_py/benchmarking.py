
from metodos_ordenamiento import metodosOrdenamiento
import time
import random


class benchmarking:


    def __init__(self):
        print("benchmarking instanciado")
        
        
    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.mO = metodosOrdenamiento()
        # arreglo = self.build_arreglo(10000)
        # b = lambda: self.mO.sort_bubble(arreglo)
        # bm = lambda:self.mO.sort_bubble_mejorado(arreglo)
        # s = lambda:self.mO.sort_seleccion(arreglo)
        # timpoN = self.contar_con_nano_time(b)
        # tiempoB = self.contar_con_nano_time(bm)
        # tiempoS = self.contar_con_nano_time(s)

        # print(f" timepo burbuja normal " + str(timpoN))
        # print(f" tiempo con burbuja mejorada "  + str(timpoN))
        # print(f" tiempo con seleccion" + str(tiempoS))

    def build_arreglo (self, tamano):
            arreglo = []
            for i in range(tamano):
                numero = random.randint(0, 999)
                arreglo.append(tamano)
            return arreglo
    def contar_con_current_time_milles(self, tarea):
            inicio = time.time()
            tarea()
            fin = time.time()
            return (fin  - inicio)
            
    def contar_con_nano_time(self, tarea):
            inicio = time.time()
            tarea()
            fin = time.time_ns()
            return (fin - inicio) / 1000000000.0
            