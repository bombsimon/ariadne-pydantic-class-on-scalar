from b import B
from pydantic import BaseModel


class A(BaseModel):
    x: "B"


A.model_rebuild()
