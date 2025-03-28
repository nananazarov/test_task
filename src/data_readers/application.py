from src.data_readers.base import BaseReader


class ApplicationReader(BaseReader):
    request_id: str
    client_type: str

    integration_name = "Application"
    is_versioned = False

    def load(self) -> None:
        self.request_id = self.data["request_id"]
        self.client_type = self.data["client_type"]
