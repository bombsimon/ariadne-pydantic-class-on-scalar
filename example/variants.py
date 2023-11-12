from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from other import C


@dataclass
class A:
    c: "C"


@dataclass
class B:
    c: "C"
