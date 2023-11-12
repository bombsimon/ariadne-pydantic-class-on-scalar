
from c import C
from pydantic import BaseModel


class B(BaseModel):
    x: "C"
