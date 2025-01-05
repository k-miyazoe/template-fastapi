from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from sample_parameter import router as sample_parameter_router
from sample_db_operation import router as sample_db_operation_router
from sample_async import router as sample_async_router
from sample_machine_learning import router as sample_machine_learning_router


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

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(sample_parameter_router)
app.include_router(sample_db_operation_router)
app.include_router(sample_async_router)
app.include_router(sample_machine_learning_router)


