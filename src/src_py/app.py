from benchmarking import benchmarking
import benchmarking as bm
from metodos_ordenamiento import metodosOrdenamiento
import matplotlib.pyplot as plt



#from metodos_ordenamiento import metodosOrdenamiento

#from benchmarking import benchmarking  ( segunda forma de importar)
#Archivo principal o main
if __name__== "__main__":
    print("Funciona")
    
    
    bench = bm.benchmarking()
    metodosO = metodosOrdenamiento()
    
    ##tam = 10000
    tamanio = [5000, 10000, 10500]
for tam in tamanio:
    arreglo_base = bench.build_arreglo(tam)
    
    metodos_dic = {
      "burbuja": metodosO.sort_bubble,
      "seleccion": metodosO.sort_seleccion,
      "burbuja_mejorada":metodosO.sort_bubble_mejorado,
    }
    
    resultados = []
    
    for nombre, fun_metodo in metodos_dic.items(): 
        tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
        tupla_resultado = (tam,nombre,tiempo_resultado)
        resultados.append(tupla_resultado)
        
        
    for tam,nombre,tiempo_resultado in resultados:
      print ( f"Tamaño: {tam}, nombre metodo: {nombre} , tiempo: {tiempo_resultado:.6f} segundos ")
        
    #bmw.benchmarking()

    # benchmarking()
      # Ejecuta el constructor
      
      
      
      # prepara datos para ser graficos
      #1 crear un diccionario o map para almacenar los resultados por metodos
tiempos_by_metodos = {
  "burbuja":[],
  "burbuja_mejorado":[],
  "seleccion":[],
  "shell":[],
  }

for tam,nombre,tiempo_resultado in resultados:
  tiempos_by_metodos[nombre].append(tiempos_by_metodos)
  
  
  plt.figure(figsize=(10,6))
  
  for tam, nombre in tiempos_by_metodos:
    nombre,  tiempos_by_metodos.items():
    plt.plot, tiempos_by_metodos,
  
  