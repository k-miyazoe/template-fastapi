from fastapi import APIRouter
import asyncio

router = APIRouter()

#　非同期処理サンプル
async def async_task():
    await asyncio.sleep(3)  # 3秒間の非同期処理をシミュレート
    return {"message": "Async task completed"}

@router.get("/async_task")
async def run_async_task():
    result = await async_task()
    return result