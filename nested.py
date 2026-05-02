from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

address = Address(
    street="123 something",
    city="Lahore",
    postal_code="5400"
)

user = User(
    id=1,
    name="Muhammad Khan",
    address=address
)

comment = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(id=2, content="2 comment"),
        Comment(id=3, content="3 comment")
    ]
)