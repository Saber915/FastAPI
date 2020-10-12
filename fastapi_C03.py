from fastapi import FastAPI

import uvicorn

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}

]


# 2. 设置默认Query参数.
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     print(type(skip))
#     return fake_items_db[skip:skip+limit]

# 3. 设置可选Query参数
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str = None):
#     if q:
#         return {'item_id': item_id, "q": q}
#     return {"item_id": item_id}

# 4. Query参数类型转换.
# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: str = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a log description"})
#     return item

# 5.同时使用Path参数和Query参数
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q:str=None, short:bool=False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a log description"})
#     return item

# 6. 必需的查询参数
# 当你需要定义一个查询参数，而且这个参数必须传入，那么你就不能为这个参数定义任意的默认值：
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=9527)
