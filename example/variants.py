from dataclasses import dataclass

from other import C


@dataclass
class A:
    c: "C"


@dataclass
class B:
    c: "C"
