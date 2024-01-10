from pydantic import BaseModel, Field


class Input(BaseModel):
    "API Interface Model to ingest inputs for target existence calculation."

    a: list[int] = Field(..., description="First list of integers.")
    b: list[int] = Field(..., description="Second list of integers.")
    target: int = Field(..., description="Target value whose existence is checked.")
