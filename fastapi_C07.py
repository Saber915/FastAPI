from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None


# @app.put("/items/{item_id}")
# async def update_item(
#         *,
#         item_id: int = Path(..., title="THe ID fo the item to get", get=0, le=1000),
#         q: str = None,
#         item: Item = None):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


# 定义多个Body参数.

# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     }
# }

# @app.put("/items/{item_id}")
# async def update_item(*, item_id: int, user: User, item: Item):
#     results = {"item_id": item_id, "item": item, "user": user}
#
#     return results


# 使用Body定义单值的请求体参数.
# @app.put("/items/{item_id}")
# async def update_item(*, item_id: int, user: User, item: Item, importance: int = Body(...)):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#
#     return results


# 嵌入单个请求体参数.
@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}

    return results


if __name__ == '__main__':
    uvicorn.run(app=app, host="localhost", port=9527)
