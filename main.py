import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="API"
)

if __name__ == "__main__":
    uvicorn.run()
