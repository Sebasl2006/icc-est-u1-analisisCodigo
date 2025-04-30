import java.util.Random;

public class BenchMarking {

    private MetodosOrdenamiento mOrdenamiento;


    
    public BenchMarking(){
        long currentMillis = System.currentTimeMillis(); // Saca la fecha
        long currentNato = System.nanoTime();

        System.out.println(currentMillis);
        System.out.println(currentNato);

        mOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(100000);
        Runnable tarea = () -> mOrdenamiento.burbujaTradicional(arreglo);

        double tiempoDuracionMiles=(medirConCurrentTimeMiles(tarea));
        double tiempoDuracionNano =(medirConNanoTime(tarea));



        System.out.println("Tiempo en milisegundos " + tiempoDuracionMiles);
        System.out.println(" Tiempo en nano segundos " + tiempoDuracionNano);
    }



    private int[] generarArregloAleatorio( int tamano){
        int arreglo[] = new int[tamano];
        Random random = new Random();
        for (int i = 0; i < tamano; i++){
            arreglo[i] = random.nextInt(9999999);

        }
        return arreglo;
    }

    public double medirConCurrentTimeMiles(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) / 1000.0;

        return tiempoSegundos;

    }


    public double medirConNanoTime (Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        double tiempoSegundos = (fin - inicio) / 1_000_000_000.0;

        return tiempoSegundos;
    }
    
}
