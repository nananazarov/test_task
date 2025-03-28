from src.data_readers.base import BaseReader


class PythonScoringReader(BaseReader):
    score: float

    integration_name: str = "PythonScoring"
    is_versioned: bool = True

    def load(self) -> None:
        self.score = float(self.data.get("score", 0.0))
