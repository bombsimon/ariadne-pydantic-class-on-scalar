from typing import Union

from variants import A, B

AorB = Union[A, B]

def serialize_aob(value: AorB) -> dict:
    return {
        "custom_serialize": True,
        "c": value.__class__.__name__,
    }
