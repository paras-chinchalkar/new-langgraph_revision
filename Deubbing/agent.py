from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langchain.graph import StateGraph,START,END
from langchain_groq import ChatGroq
import os
os.environ['GROQ_API_KEY']=os.gentev("GROQ_API_KEY")
from dotenv import load_dotenv
load_dotenv()
os.environ['LANGCHAIN_API_KEY']=os.getenv("GROQ_API_KEY")

class State(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

llm=ChatGroq(model="openai/gpt-oss-120b")

def make_default_graph():
    graph=StateGraph(State)

    def call_model(state=State):
        return {"messages":[llm.invoke(State['messages'])]}
    
    graph.add_node("agent",call_model)
    graph.add_edge(START,"agent")
    graph.add_edge('agent',END)

    agent=graph.compile()
    return agent

agent=make_default_graph()