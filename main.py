from typing import Union
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name:str
    age:int
    id:int

items = {
    0:Item(name="Edgar",age=38,id=0),
    1:Item(name="Lizette",age=38,id=1),
    2:Item(name="Ximena",age=7,id=2),
    3:Item(name="Jona",age=11,id=3)
}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int)->dict[str,int | Item]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item id: {item_id} does not exist.")
    return {"item_id": item_id, "q": items[item_id]}

@app.get("/calculator")
def calculator(x:int,y:int)->dict[str,float]:
    #the below is using the round function
    #return {"result": round(x/y,2)}
    #this one is based on a format string option
    return {"result": f"{x/y:.2f}"}

@app.post("/")
def addItem(item:Item)->dict[str,Item]:
    if item.id in items:
        raise HTTPException(status_code=400,detail=f"Item id: {item.id} already exists.")

    items[item.id]=item
    return {"added":item}