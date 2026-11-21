from fastapi import APIRouter, HTTPException

from app.schemas import Item, ItemCreate

router = APIRouter()

# In-memory store (replace with a real database later)
_items: dict[int, Item] = {}
_next_id = 1


@router.get("/", response_model=list[Item])
def list_items():
    return list(_items.values())


@router.post("/", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global _next_id
    item = Item(id=_next_id, **payload.model_dump())
    _items[_next_id] = item
    _next_id += 1
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
