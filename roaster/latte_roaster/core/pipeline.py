from latte_roaster.config import AppSettings
from latte_roaster.core.downloader import HFDownloader
from latte_roaster.core.repository import HFRepository
from latte_roaster.core.model_registry import ModelLoader
from latte_roaster.dto.context import ImportContext
from latte_roaster.dto.protocol import GrindRequest
from latte_roaster.util.exporter import TorchExporter

class RosterPipeline:
    def __init__(self, config: AppSettings):
        self.config = config
        self.downloader = HFDownloader()
        self.model_loader = ModelLoader(
            model_id=self.config.model_id,
            revision=self.config.model_version,
        )
        self.exporter = TorchExporter()

    def run(self):
        repo = HFRepository(
            model_id=self.config.model_id,
            revision=self.config.model_version,
        )

        context = ImportContext(
            request=GrindRequest(
                model_id=self.config.model_id,
                revision=self.config.model_version,
            )
        )

        snapshot = self.downloader.download(repo=repo)
        context.model = self.model_loader.load_model(snapshot=snapshot)
        context.tokenizer = self.model_loader.load_tokenizer(snapshot=snapshot)
        context.exported_program = self.exporter.export(context=context)
