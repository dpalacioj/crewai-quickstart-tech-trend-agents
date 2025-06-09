import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

# Cargar variables de entorno
load_dotenv()

# Configurar el LLM para OpenAI
def get_openai_llm():
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME"),
        api_key=os.getenv("OPENAI_API_KEY")
    )

# Configurar el LLM para Gemini
def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model_name=os.getenv("GEMINI_MODEL_NAME"),
        api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.7,
        convert_system_message_to_human=True
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
        llm=get_openai_llm(),
        allow_delegation=False
    )

def crear_sintetizador():
    try:
        # Intentar usar Gemini
        llm = get_gemini_llm()
    except Exception as e:
        print(f"Error configurando Gemini: {e}")
        print("Usando OpenAI como fallback para el sintetizador")
        # Usar OpenAI como fallback
        llm = get_openai_llm()
        
    return Agent(
        role="Comunicador de Tecnología",
        goal="Traducir información técnica compleja a explicaciones accesibles",
        backstory="""Tienes la habilidad de explicar conceptos tecnológicos complejos
        de manera que cualquier persona pueda entenderlos, independientemente
        de su conocimiento técnico previo.""",
        verbose=True,
        llm=llm,
        allow_delegation=False
    )
