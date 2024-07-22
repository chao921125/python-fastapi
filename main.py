import uvicorn
from fastapi import FastAPI
from enum import Enum
from entity import request, response

# post get put delete
app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 所有的参数路径均按照同类型放到最后匹配
@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.post("/items/")
async def create_item(item: request.Request):
    return response.response(0, "", item)

# I'm not sure it's not normal working
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080, reload=True, workers=2)
