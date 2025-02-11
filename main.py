from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Reqiest

def ola_mundo(): #Response
    return {"mensagem": "Olá Mundo!"}