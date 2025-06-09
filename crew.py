from crewai import Crew, Process
from agents import crear_investigador, crear_sintetizador
from tasks import crear_tarea_investigacion, crear_tarea_sintesis

def main():
    # Crear los agentes
    investigador = crear_investigador()
    sintetizador = crear_sintetizador()
    
    # Crear las tareas
    tarea_investigacion = crear_tarea_investigacion(investigador)
    tarea_sintesis = crear_tarea_sintesis(sintetizador, tarea_investigacion)
    
    # Crear y ejecutar el crew
    crew_tendencias = Crew(
        agents=[investigador, sintetizador],
        tasks=[tarea_investigacion, tarea_sintesis],
        verbose=True,  # Activar salida detallada
        process=Process.sequential  # Ejecutar tareas en secuencia
    )
    
    # Ejecutar el crew y obtener el resultado
    resultado = crew_tendencias.kickoff()
    
    print("\n✅ RESULTADO FINAL:")
    print(resultado)

if __name__ == "__main__":
    main()
