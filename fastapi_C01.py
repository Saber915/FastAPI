from fastapi import FastAPI
import uvicorn

app = FastAPI()


# @app.get("/me/xx")
# async def read_item_me():
#     return {"me": 'me'}


@app.get("/me/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


@app.get("/me/xx")
async def read_item_me():
    return {"me": 'me'}


@app.get("/")
async def home():
    return {"Hello World!"}


if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=9527)
