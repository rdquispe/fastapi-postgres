from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.movies import movies_router
from schemas.models import HealthResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=movies_router, prefix="/v1/movies")


@app.get("/v1/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="up")

