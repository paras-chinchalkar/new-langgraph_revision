import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.tools.retriever import create_retriever_tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langgraph.prebuilt import create_react_agent

# Load environment variables
load_dotenv()

# Ensure API Key is set
if not os.getenv("GROQ_API_KEY"):
    print("WARNING: GROQ_API_KEY not found in environment variables.")

# Initialize LLM
# Using a standard Groq model. Adjust if needed.
llm = ChatGroq(model="llama3-70b-8192")

# --- Fix 1: Correct Wikipedia Tool Setup ---
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# --- Fix 2: Reconstruct Retriever Tool ---
# Since ReAct.ipynb was empty, creating a sample retriever.
# In a real scenario, you would load your actual documents here.
texts = [
    "LangGraph is a library for building stateful, multi-actor applications with LLMs.",
    "It extends LangChain to support cyclic graphs.",
]
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_texts(texts, embeddings)
retriever = vectorstore.as_retriever()

retriever_tool = create_retriever_tool(
    retriever,
    "langgraph_search",
    "Search for information about LangGraph. Use this for specific queries about the library."
)

tools = [retriever_tool, wiki_tool]

# --- Create Agent ---
# Using prebuilt create_react_agent which handles state management
agent = create_react_agent(llm, tools=tools)

# --- Test ---
print("Running agent test...")
try:
    response = agent.invoke({"messages": [("user", "What is LangGraph and what is it used for?")]})
    print("\nAgent Response:")
    print(response["messages"][-1].content)
except Exception as e:
    print(f"\nError running agent: {e}")
