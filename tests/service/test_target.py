from containerized_microservice.service.target import TargetService
from containerized_microservice.models.api.input import Input
import pytest


@pytest.fixture
def target_service() -> TargetService:
    return TargetService()


class TestTargetService:
    @pytest.mark.parametrize(
        "input, expected_output",
        [
            (Input(a=[1, 2, 3], b=[4, 5, 6], target=9), True),
            (Input(a=[1], b=[2], target=10), False),
            (Input(a=[], b=[1, 2, 3], target=10), False),
            (Input(a=[1, 2, 3], b=[], target=10), False),
        ],
    )
    def test_target_exists(
        self, target_service: TargetService, input: Input, expected_output: bool
    ) -> None:
        actual_output = target_service.target_exists(input)
        assert actual_output is expected_output
