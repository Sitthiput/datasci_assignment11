from pydantic import BaseModel

class Compute_input(BaseModel):
    m: float
    x: float
    c: float
    
    class Config:
        orm_mode = True