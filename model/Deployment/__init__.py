from pydantic import BaseModel

class Spec(BaseModel):
    image: str
    replica: int

class Deployment(BaseModel):
    name: str
    spec: Spec