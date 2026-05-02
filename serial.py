from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    user_id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

# create a user instance

user = User(
    user_id= 1,
    name= "Muhammad Khan",
    email="123@gmail.com",
    is_active=True,
    createdAt=datetime(2026, 5, 19, 14, 30),
    address=Address(
        street = "street 123",
        city= "Lahore",
        postal_code="5400"
    ),
    tags=["premium", "gold"],
)

# using model_dump() -> dict

python_dict = user.model_dump()
print(python_dict)


# using model_dump_json()

json_str = user.model_dump_json()
print(json_str)