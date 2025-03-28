import random

from helpers import Request, Response
from src.data_readers import DataReader
from src.strategies import NewClientStrategy, PureStreamStrategy, RepeatClientStrategy


def main(request: Request) -> Response:

    data = DataReader(request.context)

    if random.random() < 0.1:
        return PureStreamStrategy(data).calculate_result()

    if data.application.client_type == "new":
        return NewClientStrategy(data).calculate_result()

    if data.application.client_type == "repeat":
        # TODO: Implement repeat_client_pilot_strategy logic here
        return RepeatClientStrategy(data).calculate_result()

    return Response(result="error", strategy_name="default decline")
