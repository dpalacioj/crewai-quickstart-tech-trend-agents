import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI

# Cargar variables de entorno
load_dotenv()

# Configurar el LLM
def get_llm():
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME"),
        api_key=os.getenv("OPENAI_API_KEY")
    )

# Crear los agentes
def crear_investigador():
    return Agent(
        role="Investigador de Tendencias Tecnológicas",
        goal="Identificar las tendencias tecnológicas más relevantes del momento",
        backstory="""Eres un experto en seguimiento de tendencias tecnológicas.
        Tu especialidad es identificar patrones emergentes y tendencias
        que están ganando terreno en el mundo tecnológico.""",
        verbose=True,
        llm=get_llm(),
        allow_delegation=False
    )

def crear_sintetizador():
    return Agent(
        role="Comunicador de Tecnología",
        goal="Traducir información técnica compleja a explicaciones accesibles",
        backstory="""Tienes la habilidad de explicar conceptos tecnológicos complejos
        de manera que cualquier persona pueda entenderlos, independientemente
        de su conocimiento técnico previo.""",
        verbose=True,
        llm=get_llm(),
        allow_delegation=False
    )
