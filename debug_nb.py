import json

notebook_path = r'c:\Users\PARAS\Downloads\agentic-ai-langraph\agents-langgraph\ReAct.ipynb'

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if 'wiki_tool' in source:
                print(f"--- Cell {i} ---")
                print(source)
                print("----------------")
except Exception as e:
    print(f"Error reading notebook: {e}")
