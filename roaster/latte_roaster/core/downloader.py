from pathlib import Path

from huggingface_hub import snapshot_download

from latte_roaster.core.repository import HFRepository
from latte_roaster.dto.protocol import GrindEvent
from latte_roaster.util import EventEmitter

class HFDownloader:

    def download(
        self,
        repo: HFRepository,
    ) -> str:

        EventEmitter.emit(event=GrindEvent(
            type="MODEL_DOWNLOAD_STARTED",
            payload={
                "model_id": repo.model_id,
                "revision": repo.revision,
            }
        ))

        path = snapshot_download(
            repo_id=repo.model_id,
            revision=repo.revision,
            local_dir="/app/model"
        )

        EventEmitter.emit(event=GrindEvent(
            type="MODEL_DOWNLOADED",
            payload={
                "model_id": repo.model_id,
                "revision": repo.revision,
                "path": path,
            }
        ))

        return path
