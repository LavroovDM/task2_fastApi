from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Лавров Евгений Александрович"}

@app.get('/tools')
async def f_indexT():
    return "Низкие навыки"

@app.get('/users')
async def f_indexU():
    return "+79343565574"