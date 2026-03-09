from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Mensagem": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

#Crie uma rota que retorne a soma de dois números passados por caminho (URL)
# num1 = 0
# num2 = 0
# soma = num1 + num2
@app.get("/soma/{num1}/{num2}")
async def soma(num1: int, num2: int):
    return {"Resultado": num1 + num2}

#Crie uma rota que retorne a subtração de dois números
@app.get("/subtracao/{num1}/{num2}")
async def sub(num1: int, num2: int):
    return{"Resultado": num1 - num2}

#Crie uma rota que retorne a multiplicação de dois números
@app.get("/multiplicacao/{num1}/{num2}")
async def mult(num1: int, num2: int):
    return{"Resultado": num1 * num2}

#Crie uma rota que retorne a divisão de dois números
@app.get("/divisao/{num1}/{num2}")
async def div(num1: int, num2: int):
    return {"Resultado": f'{num1/num2:.3}'}

#Crie uma rota que retorne o resto da divisão de dois números
@app.get("/resto/{num1}/{num2}")
async def resto(num1: int, num2: int):
    return{"Resultado": num1 % num2 }