from fastapi import FastAPI
from routes.issues import router as issues_router


app = FastAPI()

# items = [
#     { "id": 1, "name": "Item 1", "description": "This is item 1" },
#     { "id": 2, "name": "Item 2", "description": "This is item 2" },
#     { "id": 3, "name": "Item 3", "description": "This is item 3" },
# ]

# this is the home endpoint
# @app.get("/health")
# def health_check():
#     return {"status": "ok"}


# @app.get("/items")
# def get_items():
#     return items

# # to test it "http://127.0.0.1:8000/items/3"

# @app.get("/items/{item_id}")
# def get_id(item_id:int):
#     for item in items:
#         if item["id"] == item_id:
#             return item
#     return {"error": "Item not found"}


# @app.post("/items")
# def create_item(item: dict):
#     items.append(item)
#     return item

#######         initialize the router           ########
app.include_router(issues_router)