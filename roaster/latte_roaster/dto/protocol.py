from dataclasses import dataclass
from typing import Any


@dataclass
class GrindEvent:

    type: str

    payload: dict[str, Any]

    def __str__(self):
        return f"GrindEvent(type={self.type}, payload={self.payload})"
