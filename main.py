import os
import dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

dotenv.load_dotenv()


#####  fastapi dev main.py

# instantiate FastAPI class 
app = FastAPI(
    title="Agente básico",
    description="""
        Mi primer bot
        1. * Consultas a un Modelo Choere
    """,
    version="0.1.0",
)

# model schema
class Agente(BaseModel):  
    prompt: str
    




@app.post("/agente")
async def agente(request: Agente):

    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    prompt = request.prompt

# 1- Instancia de la clase ChatCohere
    llm = ChatCohere(
        api_key=COHERE_API_KEY
    )
# 2- creación de una lista de mensajes
    list_messages = [
        SystemMessage(content="Eres experto en IA, te llamas Tilin."),
        HumanMessage(content=prompt)
    ]

# 3- invocación del método invoke
    response = llm.invoke(list_messages)

    list_messages.append(response)


    return {
        "agente": list_messages[-1].content,
    }