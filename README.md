# -Jupyter-to-Deploy


Para criar o repositório dos dados
```
gh repo create
```

Aqui rodamos o 
```
uvicorn main:app --reload
```

Para validar a documentação
http://127.0.0.1:8000/docs


Depois fazemos os testes e executamos  `pytest -v testes.py`

Em seguida criamos o CI/CD e assim criamos também o arquivo requirements a partir do  
`pip freeze >> requirements-dev.txt` 