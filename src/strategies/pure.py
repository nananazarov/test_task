from .base import BaseStrategy
from helpers import Response


class PureStreamStrategy(BaseStrategy):
    def calculate_result(self) -> Response:
        return Response(
            result="1",
            score=self.data.scorecard_data.score,
            strategy_name="pure_stream_strategy",
            additional_data={},
            max_loan_duration=6,
            max_loan_amount=8000,
        )
