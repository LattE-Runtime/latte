from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from latte_roaster.dto.protocol import GrindRequest

if TYPE_CHECKING:
    from torch.export import ExportedProgram
    from transformers import PreTrainedModel, PreTrainedTokenizerBase

@dataclass
class ImportContext:
    request: GrindRequest
    model: PreTrainedModel | None = field(default=None)
    tokenizer: PreTrainedTokenizerBase | None = field(default=None)
    exported_program: ExportedProgram | None = field(default=None)
    ir: Any | None = field(default=None)
