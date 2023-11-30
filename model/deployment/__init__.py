from pydantic import BaseModel, Field
from typing import Optional


class Spec(BaseModel):
    image: str
    replica: int = Field(default=1)


class Deployment(BaseModel):
    apiVersion: Optional[str] = Field(default="apps/v1")
    name: str
    spec: Spec
