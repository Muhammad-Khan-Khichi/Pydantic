from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: int = 500
    in_stock: bool = True

input_data = {'id': 10, 'name': "Samsung"}

product = Product(**input_data)

print(product)