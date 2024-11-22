from datetime import datetime
import statistics

class Experimento: 
    
#Funcion de Inicializacion
    def __init__(self, nombreExperimento, fechaRealizacion, TipoExperimento, resultadoObtenido):
        self.nombreExperimento = nombreExperimento
        self.fechaRealizacion = fechaRealizacion
        self.TipoExperimento = TipoExperimento
        self.resultadoObtenido = resultadoObtenido



#Funcion para Agregar Datos de Experimentos 
def agregarDatos(listaExperimentos):
        nombreExperimento = input("Ingrese el nombre del experimento: ").lower()
        
        fechaRealizacion_str = input("Ingrese la fecha de realización (DD/MM/AAAA):  ")
        try: 
            fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y") 
        except ValueError:
            print("Fecha Inválida.")
            return 
        
        tiposValidos = ["biologia", "fisica", "quimica"]
        while True:
            TipoExperimento = input("Ingrese el tipo de experimento (biologia, fisica, quimica): ").lower()
            if TipoExperimento in tiposValidos:
                break
            else:
                print("Tipo de experimento no válido. Por favor, elija entre: biologia, fisica o quimica.")

        while True:  # Bucle para asegurar que se ingresen más de 3 resultados
            resultadoObtenido_str = input("Ingrese el resultado obtenido separados por comas (ej. 5,3,7): ")
            try: 
                resultadoObtenido = list(map(float, resultadoObtenido_str.split(",")))
                if len(resultadoObtenido) > 3:  # Verificar que haya más de 3 resultados
                    break
                else:
                    print("Debe ingresar más de 3 resultados. Intente nuevamente.")
            except ValueError:
                print("Valor inválido. Asegúrese de ingresar solo números separados por comas.")

        print("\nExperimento agregado exitosamente.")              
  

              
            
        #Crear un objeto Experimento y agregarlo a la lista de experimentos
        experimento = Experimento(nombreExperimento, fechaRealizacion, TipoExperimento, resultadoObtenido)
        listaExperimentos.append(experimento)  
                 
  
#Funcion para Visualizar Datos             
def visualizarDatos(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        return
            
    for i, experimento in enumerate(listaExperimentos, start = 1):
       print(f"\nExperimento {i}")    
       print(f"  Nombre del Experimento: {experimento.nombreExperimento}")    
       print(f"  Fecha de realizacion: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}") 
       print(f"  Tipo de Experimento: {experimento.TipoExperimento}")    
       print(f"  Resultado obtenido: {experimento.resultadoObtenido}")     

# Funcion para Eliminar Experimentos               
def eliminarExperimentos(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        return
    
    opcionEliminar = input("Ingrese el nombre del experimento que desea eliminar: ").lower()
    
    # Bandera para saber si se encontro el experimento
    experimentoEliminado = False
    
    # Recorremos la lista de experimentos
    for experimento in listaExperimentos:
        if experimento.nombreExperimento == opcionEliminar:
            listaExperimentos.remove(experimento)
            print("\nExperimento eliminado con exito.")
            experimentoEliminado = True
            break  # Si lo encontramos, no es necesario seguir buscando.
    
    if not experimentoEliminado:
        print("Experimento no encontrado.")

    
    
# Funcion para analizar los resultados 
def analisisResultados(listaExperimentos):
    if not listaExperimentos:
        print("Experimento no encontrado.")
        return
    
    resultadosTotales = []
    for experimento in listaExperimentos:
        resultadosTotales.extend(experimento.resultadoObtenido)   
     
    while True:
        print("\nOperaciones Basicas de los resultados")  
        print("1. Promedio: ") 
        print("2. Maximo: ")
        print("3. Minimo: ")
        print("4. Volver: ")
         
        opcion = input("Digite una opcion: ")
        if opcion == "1":
            if resultadosTotales:
             promedio = statistics.mean(resultadosTotales)
             print(f"Promedio de todos los resultados: {promedio}")
            else:
                print("No hay resultados para analizar.")
                
        elif opcion == "2":
              if resultadosTotales:
                maximo = max(resultadosTotales)
                print(f"Maximo de todos los resultados: {maximo}")
              else:
                  print("No hay resultados para analizar.")  
                  
        elif opcion == "3":
              if resultadosTotales:
                minimo = min(resultadosTotales)
                print(f"Minimo de todos los resultados: {minimo}")
              else:
                  print("No hay resultados para analizar.")  
        elif opcion == "4":
           return
        else:
            print("Opcion Invalidad")
            
# Función para comparar dos o más experimentos
def comparaExperimentos(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados para comparar.")
        return

    # Solicitar los nombres de los experimentos a comparar
    nombres = input("Ingrese los nombres de los experimentos que desea comparar, separados por comas: ").lower()
    nombresListas = [nombre.strip() for nombre in nombres.split(",")]

    # Filtrar los experimentos seleccionados
    experimentosSeleccionados = [exp for exp in listaExperimentos if exp.nombreExperimento in nombresListas]

    # Verificar si hay al menos dos experimentos válidos
    if len(experimentosSeleccionados) < 2:
        print("Debe seleccionar al menos dos experimentos válidos para comparar.")
        # Mostrar los experimentos que no fueron encontrados
        experimentosNoEncontrados = [nombre for nombre in nombresListas if nombre not in [exp.nombreExperimento for exp in experimentosSeleccionados]]
        if experimentosNoEncontrados:
            print(f"Los siguientes experimentos no se encontraron: {', '.join(experimentosNoEncontrados)}")
        return

    print("\nComparación de Experimentos:")
    for i, experimento in enumerate(experimentosSeleccionados, start=1):
        print(f"  {i}. {experimento.nombreExperimento} - Resultados: {experimento.resultadoObtenido}")

    # Comparar resultados (este código recorre todos los experimentos seleccionados y genera tres diccionarios)
    maximos = {exp.nombreExperimento: max(exp.resultadoObtenido) for exp in experimentosSeleccionados}
    minimos = {exp.nombreExperimento: min(exp.resultadoObtenido) for exp in experimentosSeleccionados}
    promedios = {exp.nombreExperimento: sum(exp.resultadoObtenido) / len(exp.resultadoObtenido) for exp in experimentosSeleccionados}

    # Identificar el mejor y peor resultado en general
    mejorExperimento = max(maximos, key=maximos.get)
    peorExperimento = min(minimos, key=minimos.get)

    print("\nResultados de la comparación:")
    for nombre in maximos:
        print(f"  - {nombre}:")
        print(f"    Máximo: {maximos[nombre]}")
        print(f"    Mínimo: {minimos[nombre]}")
        print(f"    Promedio: {promedios[nombre]:.2f}")

    print(f"\nEl experimento con el mejor resultado general es '{mejorExperimento}' con un máximo de {maximos[mejorExperimento]}.")
    print(f"El experimento con el peor resultado general es '{peorExperimento}' con un mínimo de {minimos[peorExperimento]}.")





# Generar un informe sobre los experimentos y sus estadisticas                      
def generarInforme(listaExperimentos):
    # Abrir archivo de texto para escribir el informe
    with open("informe_experimentos.txt", "w") as archivo:
        # Escribir cabecera
        archivo.write("Informe de Experimentos. \n")
        archivo.write("=" * 50 + "\n\n")
        
        # Variable para las conclusiones
        conclusiones = []
        
        # Recorrer cada experimento para escribir su descripción y estadísticas
        for experimento in listaExperimentos:
            archivo.write(f"Nombre: {experimento.nombreExperimento}\n")
            archivo.write(f"Fecha: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Tipo: {experimento.TipoExperimento}\n")
            archivo.write(f"Resultados: {experimento.resultadoObtenido}\n")
            
            # Calcular estadísticas básicas
            resultados = experimento.resultadoObtenido
            promedio = sum(resultados) / len(resultados)
            maximo = max(resultados)
            minimo = min(resultados)
            
            archivo.write(f"Promedio de resultados: {promedio}\n")
            archivo.write(f"Valor máximo: {maximo}\n")
            archivo.write(f"Valor mínimo: {minimo}\n")
            
            # Agregar conclusiones
            if maximo == resultados[0]:  # O si el máximo es mayor que todos los demás resultados
                conclusiones.append(f"El experimento {experimento.nombreExperimento} obtuvo los mejores resultados.")
            if minimo == resultados[0]:  # O si el mínimo es menor que todos los demás
                conclusiones.append(f"El experimento {experimento.nombreExperimento} obtuvo los peores resultados.")
            
            archivo.write("-" * 50 + "\n\n")
        
        # Escribir conclusiones generales
        archivo.write("Conclusiones:\n")
        for conclusion in conclusiones:
            archivo.write(f"- {conclusion}\n")
        
    print("Informe generado exitosamente.")



# Esta funcion nos permite controlar el flujo general del sistema 

def menu():
    
     listaExperimentos = []
     while True:
      print("\nMenu de Opciones")  
      print("1. Agregar un Experimento: ") 
      print("2.Visualizar Experimentos: ")
      print("3. Eliminar un Experimento: ")
      print("4. Calcular Estadisticas: ")
      print("5. Comparar experimentos: ")
      print("6. Generar Informe: ")
      print("7. Salir.")
     
      opcion = input("Digite una opcion: ")
    
      if opcion =="1":
              agregarDatos(listaExperimentos) 

      elif opcion == "2":
             visualizarDatos(listaExperimentos)
          
      elif opcion == "3":
            eliminarExperimentos(listaExperimentos)
      elif opcion == "4":
            analisisResultados(listaExperimentos)
      elif opcion == "5":
          comparaExperimentos(listaExperimentos)      
      elif opcion == "6":
            generarInforme(listaExperimentos)   
      elif opcion == "7": 
          print("\nGracias por usar.")  
          break       
     

if __name__ == "__main__":
    menu()