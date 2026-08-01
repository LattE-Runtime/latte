from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from torch.export import ExportedProgram
    from latte_roaster.dto.context import ImportContext

class GraphExporter(ABC):

    @abstractmethod
    def export(self, context: ImportContext) -> ExportedProgram: ...

class TorchExporter(GraphExporter):
    
    def export(self, context: ImportContext) -> ExportedProgram:
        import torch

        if context.model is None:
            raise ValueError("ImportContext.model must be set before export")
        if context.tokenizer is None:
            raise ValueError("ImportContext.tokenizer must be set before export")

        example_inputs = self._build_example_inputs(context)

        from latte_roaster.dto.protocol import GrindEvent
        from latte_roaster.util.emitter import EventEmitter

        EventEmitter.emit(GrindEvent(
            type="EXPORT_STARTED",
            payload={"model_id": context.request.model_id},
        ))

        exported: ExportedProgram = torch.export.export(
            context.model,
            args=(),
            kwargs=example_inputs,
        )

        EventEmitter.emit(GrindEvent(
            type="EXPORT_COMPLETE",
            payload={"model_id": context.request.model_id},
        ))

        return exported

    def _build_example_inputs(self, context: ImportContext) -> dict:
        inputs = context.tokenizer("Hello", return_tensors="pt")
        return {**dict(inputs), "use_cache": False}
