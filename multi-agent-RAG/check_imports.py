
import sys

log = open("import_check.log", "w")
sys.stdout = log
sys.stderr = log

try:
    from langchain_community.prompt import PromptTemplate
    print("Found in langchain_community.prompt")
except ImportError as e:
    print(f"Error 1: {e}")

try:
    from langchain_core.prompts import PromptTemplate
    print("Found in langchain_core.prompts")
except ImportError:
    print("Not found in langchain_core.prompts")

try:
    from langchain.prompts import PromptTemplate
    print("Found in langchain.prompts")
except ImportError:
    print("Not found in langchain.prompts")

try:
    from langchain.agents import create_react_agent
    print("Found in langchain.agents")
except ImportError:
    print("Not found in langchain.agents")

try:
    from langgraph.prebuilt import create_react_agent
    print("Found in langgraph.prebuilt")
except ImportError:
    print("Not found in langgraph.prebuilt")

log.close()
