from fastapi.testclient import TestClient
from containerized_microservice.app import app
from typing import Union
import pytest


@pytest.fixture
def test_client() -> TestClient:
    return TestClient(app)


class TestTargetAPI:
    @pytest.mark.parametrize(
        "json_input, expected_status_code, expected_result",
        [
            ({"a": [1, 2, 3], "b": [4, 5, 6], "target": 7}, 200, True),
            ({"a": [1, 2, 3], "b": [4, 5, 6], "target": 100}, 200, False),
            ({"a": [1, 2, 3], "b": [4, 5, 6]}, 422, False),
            ({"a": [1, 2, 3], "b": [4, 5, 6], "target": "five"}, 422, False),
            ({"a": ["one", "two", "three"], "b": [4, 5, 6], "target": 5}, 422, False),
            ({}, 422, False),
        ],
    )
    def test_target_api(
        self,
        test_client: TestClient,
        json_input: dict[str, Union[list[int], int]],
        expected_status_code: int,
        expected_result: bool,
    ) -> None:
        response = test_client.post("/v1/target-exists", json=json_input)
        assert response.status_code == expected_status_code

        if response.status_code == 200:
            assert response.json() is expected_result
