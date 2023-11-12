from dataclasses import dataclass

from c import C


@dataclass
class B:
    x: "C"
