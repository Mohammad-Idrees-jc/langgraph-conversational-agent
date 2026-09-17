from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",
    huggingfacehub_api_token=HF_TOKEN,
    task = "text_generation")

model = ChatHuggingFace(llm=llm)

class ChatState(TypedDict):
  messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
  # Take user querry from state
  messages = state["messages"]
  # Send to llm
  response = model.invoke(messages)
  # Response store state
  return {"messages": [response]}


check_pointer = InMemorySaver()
graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chat_bot = graph.compile(checkpointer=check_pointer)
