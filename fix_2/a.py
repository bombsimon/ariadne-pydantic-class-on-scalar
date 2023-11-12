from b import B
# ruff: noqa: F401
from c import C
from pydantic import BaseModel


class A(BaseModel):
    x: "B"


A.model_rebuild()
