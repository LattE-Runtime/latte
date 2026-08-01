from transformers import AutoModelForCausalLM, AutoTokenizer

from latte_roaster.dto.protocol import GrindEvent
from latte_roaster.util.emitter import EventEmitter


class ModelLoader:
    def __init__(self, model_id: str, revision: str = "main"):
        self.model_id = model_id
        self.revision = revision

    def load_model(self, snapshot: str):
        model = AutoModelForCausalLM.from_pretrained(
            snapshot,
            trust_remote_code=False,
        )

        EventEmitter.emit(event=GrindEvent(
            type="MODEL_LOADED",
            payload={
                "model_id": self.model_id,
                "revision": self.revision,
            }
        ))

        return model

    def load_tokenizer(self, snapshot: str):
        tokenizer = AutoTokenizer.from_pretrained(
            snapshot,
            trust_remote_code=False,
        )

        EventEmitter.emit(GrindEvent(
            type="TOKENIZER_LOADED",
            payload={
                "model_id": self.model_id,
                "revision": self.revision,
            }
        ))

        return tokenizer
