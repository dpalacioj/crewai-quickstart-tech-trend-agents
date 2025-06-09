import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Cargar variables de entorno
load_dotenv()

# Configurar los LLMs
openai_llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL_NAME"),
    api_key=os.getenv("OPENAI_API_KEY")
)

# Crear los agentes
investigador = Agent(
    role="Investigador de Tendencias Tecnológicas",
    goal="Identificar las tendencias tecnológicas más relevantes del momento",
    backstory="""Eres un experto en seguimiento de tendencias tecnológicas.
    Tu especialidad es identificar patrones emergentes y tendencias
    que están ganando terreno en el mundo tecnológico.""",
    verbose=True,
    llm=openai_llm,
    allow_delegation=False
)

sintetizador = Agent(
    role="Comunicador de Tecnología",
    goal="Traducir información técnica compleja a explicaciones accesibles",
    backstory="""Tienes la habilidad de explicar conceptos tecnológicos complejos
    de manera que cualquier persona pueda entenderlos, independientemente
    de su conocimiento técnico previo.""",
    verbose=True,
    llm=openai_llm,
    allow_delegation=False
)

# Definir las tareas
tarea_investigacion = Task(
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

tarea_sintesis = Task(
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
