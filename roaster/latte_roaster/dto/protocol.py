from dataclasses import dataclass
from enum import Enum
from typing import Any


@dataclass
class GrindEvent:
    type: str
    payload: dict[str, Any]

    def __str__(self):
        return f"GrindEvent(type={self.type}, payload={self.payload})"

@dataclass
class GrindRequest:
    model_id: str
    revision: str = "main"
    output_path: str = "/app/output"

@dataclass
class IRFormat(Enum):
    ONNX = "onnx"       # Opted for POC
    LATTE = "latte"     # TODO Stratgic path ahead

