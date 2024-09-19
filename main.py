import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title="API",
    summary="API",
    description="API",
    version="0.1.0",
    generate_unique_id_function=custom_generate_unique_id
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins (or "*" for all)
    allow_credentials=True,  # Whether to allow cookies or authentication headers
    allow_methods=["*"],  # List of HTTP methods allowed (GET, POST, etc.)
    allow_headers=["*"],  # List of allowed headers
)

if __name__ == "__main__":
    uvicorn.run()
