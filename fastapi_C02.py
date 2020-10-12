from fastapi import FastAPI
from enum import Enum

import uvicorn

app = FastAPI()


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get('/model/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"who": model_name, 'message': 'Deep learning FTW!'}
    if model_name.value == '李四':
        return {"who": model_name, 'message': 'LeCNN all the images'}
    return {'who': model_name, 'message': 'Have some residuals'}


@app.get("/")
async def home():
    return {"Hello World!"}


if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=9527)
