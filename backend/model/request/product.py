from pydantic import BaseModel
from typing import Optional



class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    category_id: int
    image: Optional[str] = None
    rating: Optional[int] = None
    number_of_ratings: Optional[int] = None
 