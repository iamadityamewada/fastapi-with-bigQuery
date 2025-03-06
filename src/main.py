from fastapi import FastAPI
from src.router import router



app = FastAPI(
    title="Experiment",
    version="1.0.0",
    docs_url="/docs",  # Custom path for Swagger documentation
)


app.include_router(router)

@app.get("/")
async def Main():
    return {"message": "Project is live"}