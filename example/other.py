import time
from dataclasses import dataclass

# I'm expensive to import
time.sleep(30)


@dataclass
class C:
    x: str
