from fastapi import FastAPI, Query
import uvicorn
from typing import List

app = FastAPI()


# 可选参数q
# @app.get("/items")
# async def read_item(q: str = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Query参数验证, min_length, max_length
# @app.get("/items/")
# async def read_items(q: str = Query(None, min_length=3, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# 5. 正则验证
# @app.get("/items/")
# async def read_items(q: str = Query(None, regex="^fixedquery$")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# 6. 设置默认值.
# @app.get("/items/")
# async def read_items(q: str = Query("fixedquery", min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# 7. 查询参数为必需.
# @app.get("/items/")
# async def read_items(q: str = Query(..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 8. 查询参数多次出现.
# @app.get("/items/")
# async def read_items(q: List[str] = Query(None)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# 9. 列表多个值, 设置默认参数.
# @app.get("/items/")
# async def read_items(q: List[str] = Query(["Saber", "Lancer"])):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# 10. 使用list, 但是fastApi不会检查list中的内容
# @app.get("/items/")
# async def read_items(q: list = Query(["Saber", "Lancer"])):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# 11. title, description
# @app.get("/items/")
# async def read_items(q: str = Query(None,
#                                     title="query string",
#                                     description="Query string for the items to search in the database that have a good match",
#                                     min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# 12 别名参数
@app.get("/items/")
async def read_items(q: str = Query(None,
                                    title="query string",
                                    description="Query string for the items to search in the database that have a good match",
                                    alias="item-query",
                                    min_length=3,
                                    deprecated=True
                                    )):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=9527)
