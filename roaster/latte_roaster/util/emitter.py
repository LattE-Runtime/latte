import json

from latte_roaster.dto.protocol import GrindEvent


class EventEmitter:

    @classmethod
    def emit(cls, event: GrindEvent):

        print(event, flush=True)
