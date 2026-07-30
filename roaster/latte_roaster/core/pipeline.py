from latte_roaster.config import AppSettings
from latte_roaster.core.downloader import HFDownloader
from latte_roaster.core.repository import HFRepository


class RosterPipeline:
    def __init__(self, config: AppSettings):
        self.config = config
        self.downloader = HFDownloader()

    def run(self):
        repo = HFRepository(
            model_id=self.config.model_id,
            revision=self.config.model_version,
        )

        self.downloader.download(repo=repo)
