import logging

from fastapi import FastAPI

from app.router.author import author_router
from app.router.book import book_router

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(author_router)
    application.include_router(book_router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("***Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("***Shutting down...")
