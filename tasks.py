from crewai import Task

# Definir las tareas
def crear_tarea_investigacion(investigador):
    return Task(
        description="""Investiga las 3 tendencias tecnológicas más importantes en 2025.
        Para cada tendencia incluye:
        - Nombre de la tendencia
        - Breve descripción
        - Por qué es importante ahora
        - Empresas principales que están trabajando en esto
        
        Responde de manera estructurada y organizada.
        """,
        agent=investigador,
        expected_output="Un informe estructurado con las 3 principales tendencias tecnológicas de 2025"
    )

def crear_tarea_sintesis(sintetizador, tarea_investigacion):
    return Task(
        description="""Basándote en la investigación proporcionada, crea una explicación
        fácil de entender para alguien sin conocimiento técnico.
        
        Tu explicación debe:
        - Usar analogías cotidianas para explicar cada tecnología
        - Evitar jerga técnica compleja
        - Explicar por qué estas tendencias son importantes para la persona común
        - Incluir un párrafo final sobre cómo estas tendencias podrían cambiar nuestra vida diaria
        
        Tu audiencia son personas sin conocimiento técnico que quieren entender por qué
        estas tendencias son relevantes para ellos.
        """,
        agent=sintetizador,
        expected_output="Una explicación clara y accesible de las tendencias tecnológicas para audiencia no técnica",
        context=[tarea_investigacion]
    )
