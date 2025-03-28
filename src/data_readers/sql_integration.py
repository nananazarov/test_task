from src.data_readers.base import BaseReader


class SQLIntegrationReader(BaseReader):
    name: str
    age: int
    sex: str
    document_id: str
    address: str
    # TODO: add phone number

    integration_name: str = "SqlIntegration"
    is_versioned: bool = False

    def load(self) -> None:
        self.name = self.data.get("name", "")
        self.age = int(self.data.get("age", 0))
        self.sex = self.data.get("sex", "")
        self.document_id = self.data.get("document_id", "")
        self.address = self.data.get("address", "")
