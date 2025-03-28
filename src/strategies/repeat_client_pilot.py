from .base import BaseStrategy
from helpers import Response


class RepeatClientPilotStrategy(BaseStrategy):
    def calculate_result(self) -> Response:
        if self.data.scorecard_data.score < 0.42:
            return Response(
                result="1",
                score=self.data.scorecard_data.score,
                strategy_name="repeat_client_pilot_strategy",
                additional_data={},
                max_loan_duration=10,
                max_loan_amount=12000,
            )
        return Response(result="0", strategy_name="repeat_client_pilot_strategy")
