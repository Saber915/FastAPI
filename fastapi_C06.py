from fastapi import FastAPI, Path, Query
import uvicorn

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#         *,
#         q: str,
#         item_id: int = Path(..., title="the ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# 数组验证: 大于或等于
@app.get("/items/{item_id}")
async def read_items(
        *,
        q: str,
        item_id: int = Path(..., title="the ID of the item to get", ge=2)):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=9527)
