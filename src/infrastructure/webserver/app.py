from starlette import status
from fastapi import FastAPI, HTTPException

from src.application.exceptions import ApplicationException, NotFound
from src.infrastructure.webserver.routers import user_router, sensor_router

app = FastAPI(
    title="API",
    openapi_url="/docs/openapi.json",
    docs_url="/docs/swagger.yml",
    root_path="/api"
)


@app.exception_handler(NotFound)
async def not_found_exception_handler(request, exc):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=exc.message
    )


@app.exception_handler(ApplicationException)
async def application_exception_handler(request, exc):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=exc.message
    )


app.include_router(user_router, prefix="/users")
app.include_router(sensor_router, prefix="/sensors")
