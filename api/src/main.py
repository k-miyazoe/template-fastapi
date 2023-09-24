from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from typing import Union

app = FastAPI(
    title="api title(need to change)",
    description="Initial Template FastAPI.",
    version="1.0",
)

load_dotenv()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

# クエリパラメータ有り
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# パスパラメータとクエリパラメータ有り
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# 複数のパスパラメータとクエリパラメータ有り
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# 必須のクエリパラメータ
@app.get("/items-needy/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
