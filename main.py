from typing import Union
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name:str
    age:int
    id:int
    # def __init__(self,name,age):
    #     self.name= name
    #     self.age=age

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

Selection = dict[
    str, str | int | None
]  # dictionary containing the user's query arguments

@app.get("/items")
def query_by_parameters(
    name: str | None = None,
    age:int | None=None
)->dict[str,Selection | list[Item]]:
    #Creating a function inside of the controller function
    def check_item(item: Item):
        
        """ 
            all function returns true if all items are true
            in this case we validate name as none to make sure 
            return true even when there is no  parameter
        """
        return all(
            [
                name is None or item.name==name,
                age is None or item.age==age
            ]
        )
    selection=[item for item in items.values() if check_item(item)]
    return{
        "query":{"name":name, "age":age},
        "result":selection
    }

@app.post("/")
def addItem(item:Item)->dict[str,Item]:
    if item.id in items:
        raise HTTPException(status_code=400,detail=f"Item id: {item.id} already exists.")

    items[item.id]=item
    return {"added":item}