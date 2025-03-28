from .base import BaseStrategy
from helpers import Response


class RepeatClientStrategy(BaseStrategy):
    def calculate_result(self) -> Response:
        if self.data.scorecard_data.score < 0.35:
            return Response(
                result="1",
                score=self.data.scorecard_data.score,
                strategy_name="repeat_client_strategy",
                additional_data={},
                max_loan_duration=12,
                max_loan_amount=15000,
            )
        return Response(result="0", strategy_name="repeat_client_strategy")
