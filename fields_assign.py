from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=1,
        max_length=3,
        description="Employee Name",
        examples="Muhammad Khan"
        )
    dept: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000
        )