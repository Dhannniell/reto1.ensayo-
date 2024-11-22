from datetime import datetime
import statistics

class Tarea:
    # Funcion de inicializacion = metodo constructor 
    
    def __init__(self, nombre, fechaLimite, categoria, horasDedicadas):
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categoria = categoria
        self.horasDedicadas = horasDedicadas
        
        
        
#funcion para agragar una tarea 

def agregarTarea(listaTareas):
    nombre = input("Ingrese el nombre de la tarea: ")
    fechaLimite_str = input("Ingrese la fecha limite de la tarea (DD/MM/AAAA): ")
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, "%d/%m/%Y")
    except ValueError:
        print("Fecha no válida.")
        return

    categoria = input("Ingrese la categoría de la tarea (Personal, Trabajo, Estudio): ")
    horasDedicadas_str = input("Ingrese las horas dedicadas separadas en comas ej; 2,5,9: ")
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(",")))
    except ValueError:
        print("Horas no válidas.")
        return

    # Crear un objeto Tarea y agregarlo a la lista
    tarea = Tarea(nombre, fechaLimite, categoria, horasDedicadas)
    listaTareas.append(tarea)
    print("¡Tarea agregada con éxito!")
    
 #crear un objeto y lo agrega a la lista de tareas 
 
    tarea = Tarea(nombre, fechaLimite, categoria, horasDedicadas)
    listaTareas.append(tarea)
    print("Tarea agregada con exito! ")
    
def visualizarTareas(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas.")
        return
        
    for i, tarea in enumerate(listaTareas, start=1):
        print(f"\nTarea {i}  ")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha Limite: {tarea.fechaLimite.strftime("%d/%m/%Y")}")
        print(f"Categoria: {tarea.categoria}")
        print(f"Horas Dedicadas: {tarea.horasDedicadas}")
 
        
        
def analizarHoras(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas.")
        return
    
    for  tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f"\nAnalisis de {tarea.nombre}")
        print(f"Promedio de horas {promedio}")
        print(f"Maximo de Horas {maximo}")
        print(f"Minimo de Horas {minimo}")
        print("\n")
        
def generarInforme(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas.")
        return
    
    #abrir un archivo txt para escribir un informe
    with open("Informe_Tareas.txt", "w") as archivo:
         #escribir los detalles de la tarea en el archivo
        for  tarea in listaTareas:
            archivo.write(f"Nombre: {tarea.nombre}\n")
            archivo.write (f"Fecha Limite: {tarea.fechaLimite.strptime("%d/%m/%Y")}\n")
            archivo.write(f"Categoria: {tarea.categoria}\n")
            archivo.write((f"Horas Dedicadas: {tarea.horasDedicadas}\n"))
            archivo.write("\n")
            print("Informe Generado! Informe_Tareas.txt :)")        
    
    
def menu():

    listaTareas = []
    while True:
       print("\nMenu de opciones")
       print("1. Agregar tarea: ")
       print("2. Visualizar tareas: ")
       print("3. Analizar horas dedicadas: ")
       print("4. Generar informe: ")
       print("5. Salir: ")
       
       
       opcion =  input(print("digite una opcion: "))
       
       if opcion == "1":
           agregarTarea(listaTareas)
           
       elif opcion == "2":
            visualizarTareas(listaTareas)
           
       elif opcion == "3":
          analizarHoras(listaTareas)
          
       elif opcion == "4":
           generarInforme(listaTareas)
           
       elif opcion == "5":     
           print("Sesion finalizada...")
           break
       else:
           print("Opcion Invalida.")
           
if __name__ == "__main__":
    menu()