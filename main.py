from fastapi import FastAPI

app=FastAPI()

a=9
b=8
print(a+b)
@app.get('/')
async def index():
    return {"data":{"name":"mohini","company":"IAM","position":"Embedded Software developer","EID":1045}}

@app.get('/about')
def about():
    return {'data':"Mohini"}
