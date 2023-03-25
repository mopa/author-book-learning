from fastapi import APIRouter

book_router = APIRouter(prefix="/book", tags=["book"])

@book_router.get("/")
async def get_book():
    return {"book": "I Robot"}

@book_router.post("/")
async def create_book():
    return {"book": "I Robot"}

@book_router.put("/{book_id}")
async def update_book():
    return {"book": "I Robot"}

@book_router.delete("/")
async def delete_book():
    return {"book": "I Robot"}

@book_router.get("/{book_id}")
async def get_book_by_id(book_id: int):
    return {"book_id": book_id}

