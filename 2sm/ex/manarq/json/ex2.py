import json
import os 

try: 
    usuarios = {}
    if os.path.exists('d:usuarios.json'):
        with open('d:/usuarios.json','r',encoding='utf-8') as f:
            usuarios = json.loads(f.read())
except FileExistsError:
    print("arquivo não encontrado")