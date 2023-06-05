from fastapi import FastAPI, Query
from fastapi.middleware import cors
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import mysql.connector

app = FastAPI()

# Configurar CORS para permitir solicitudes desde el frontend
app.add_middleware(cors.CORSMiddleware, allow_origins=["http://localhost:8080"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


# Configurar la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2112",
    database="crud"
)

# Modelo de datos utilizando Pydantic
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: str

# Rutas de la API
@app.get("/items", response_model=List[Item])
def read_items(search: str = Query(None)):
    cursor = db.cursor()    
    if search:
        cursor.execute(
            "SELECT id, name, description FROM items WHERE name LIKE %s OR description LIKE %s",
            (f"%{search}%",f"%{search}%")
        )
    else:
        cursor.execute("SELECT id, name, description FROM items")
        
    items = []
    for (id, name, description) in cursor:
        items.append({"id": id, "name": name, "description": description})
        
    cursor.close()
    return items

@app.post("/items", response_model=Item)
def create_item(item: Item):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO items (name, description) VALUES (%s, %s)",
        (item.name, item.description)
    )
    db.commit()
    item.id = cursor.lastrowid
    cursor.close()
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE items SET name=%s, description=%s WHERE id=%s",
        (item.name, item.description, item_id)
    )
    db.commit()
    cursor.close()
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM items WHERE id=%s", (item_id,))
    db.commit()
    cursor.close()
    return {"message": "Item deleted"}

# Ejecutar el servidor con Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)