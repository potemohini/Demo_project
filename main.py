from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def index():
    return {"data":{"name":"mohini","company":"IAM","position":"Embedded Software developer","EID":1045}}

@app.get('/about')
def about():
    return {'data':"Mohini"}
