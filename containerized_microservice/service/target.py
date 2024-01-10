from containerized_microservice.models.api.input import Input
import logging


class TargetService:
    """Service class for tasks which are related to the target endpoint."""

    logger = logging.getLogger(__name__)

    def target_exists(self, input: Input) -> bool:
        """Checks if target exists on given input.

        This method checks if the sum of an integer from list a and an
        integer from list b results in the target value.

        Args:
            input: The two lists which should be checked for existence of the
                target value.

        Returns:
            True, if the target value exists in the given input. False otherwise.
        """
        self.logger.debug(f"Calculating result for given input <{input}>")

        result = False
        for a in input.a:
            for b in input.b:
                if a + b == input.target:
                    result = True
                    break

        self.logger.debug(f"Calculated result <{result}> for given input <{input}>")
        return result
