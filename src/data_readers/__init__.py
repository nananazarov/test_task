from pathlib import Path
from .application import ApplicationReader
from .sql_integration import SQLIntegrationReader
from .python_scoring import PythonScoringReader


class DataReader:
    application = ApplicationReader
    user_data = SQLIntegrationReader
    scorecard_data = PythonScoringReader

    def __repr__(self) -> str:
        return f"DataReader({str(self.application)}, {str(self.user_data)}, {str(self.scorecard_data)})"

    def __init__(self, root: Path) -> None:
        self.application = ApplicationReader(root)
        self.user_data = SQLIntegrationReader(root)
        self.scorecard_data = PythonScoringReader(root)


__all__ = ["DataReader"]
