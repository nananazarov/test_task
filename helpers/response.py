from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Literal


@dataclass
class Response:
    result: Literal["1", "0", "error"] = field(default="0")
    score: float = field(default=0.0)
    strategy_name: str = field(default="")
    additional_data: Dict[Any, Any] = field(default_factory=dict)

    max_loan_duration: int = field(default=0)
    max_loan_amount: float = field(default=0.0)

    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "result": self.result,
            "score": self.score,
            "strategy_name": self.strategy_name,
            "additional_data": self.additional_data,
            "created_at": datetime.strftime(self.created_at, "%Y-%m-%d %H:%M:%S"),
        }
