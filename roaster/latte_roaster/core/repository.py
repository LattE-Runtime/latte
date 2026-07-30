from dataclasses import dataclass


@dataclass(slots=True)
class HFRepository:
    model_id: str
    revision: str = "main"
    trust_remote_code: bool = True
