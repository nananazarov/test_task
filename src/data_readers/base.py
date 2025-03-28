from abc import ABC, abstractmethod
import json
from pathlib import Path
from typing import Any, Dict


class BaseReader(ABC):
    integration_name: str = ""
    is_versioned: bool = False
    data: Dict[str, Any] = dict()
    root: Path
    file_path: Path

    @abstractmethod
    def load(self) -> None:
        pass

    def __init__(self, root: Path) -> None:
        self.root = root
        self.__get_file_path()
        self.__read_file()

        self.load()

        self.__after_init()

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        class_attrs = ", ".join(
            f"{k}={v}" for k, v in self.__dict__.items() if not k.startswith("__")
        )
        return f"{class_name}({class_attrs})"

    def __get_file_path(self):
        if not self.is_versioned:
            self.file_path = self.root / self.integration_name / f"{self.integration_name}.json"
        else:
            versioned_files = list(self.root.glob(f"{self.integration_name}*"))
            if not versioned_files:
                raise FileNotFoundError(f"No versioned files found for {self.integration_name}")
            file_name = versioned_files[0].name
            self.file_path = self.root / file_name / f"{file_name}.json"

    def __read_file(self) -> Dict[str, Any]:
        self.data = json.loads(self.file_path.read_text())
        return self.data

    def __after_init(self):
        self.file_path = None  # type: ignore
        self.root = None  # type: ignore
        self.integration_name = None  # type: ignore
        self.is_versioned = None  # type: ignore
        self.data = None  # type: ignore

        del self.file_path
        del self.root
        del self.integration_name
        del self.is_versioned
        del self.data
