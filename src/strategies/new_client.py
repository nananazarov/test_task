from .base import BaseStrategy
from helpers import Response


class NewClientStrategy(BaseStrategy):
    def calculate_result(self) -> Response:
        if self.data.scorecard_data.score < 0.2:
            return Response(
                result="1",
                score=self.data.scorecard_data.score,
                strategy_name="new_client_strategy",
                additional_data={},
                max_loan_duration=3,
                max_loan_amount=5000,
            )
        return Response(result="0", strategy_name="new_client_strategy")
