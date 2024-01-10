from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated
from containerized_microservice.models.api.input import Input
from containerized_microservice.service.target import TargetService

router = APIRouter()


@router.post(
    "/target-exists",
    response_model=bool,
    summary="Check if the given lists contain the target.",
    description="""This endpoint checks if the sum of an integer from list a 
        and an integer from list b results in the target value.""",
    response_description="True if target exists, false otherwise.",
)
async def target_exists(
    input: Input, target_service: Annotated[TargetService, Depends(TargetService)]
) -> bool:
    """Endpoint to check if target exists in provided lists.

    Args:
        input: The two lists which should be checked for existence of the
            target value.
        target_service: Target Service, which contains the business logic to
            check if the target exists in the provided lists.

    Returns:
        True, if the target value exists in the given input. False otherwise.
    """
    return target_service.target_exists(input)
