from pydantic import BaseModel, Field


class Salutes(BaseModel):
    """
    A list of salutes used in the game.
    """
    salutes: list[str] = Field(example=["Rock on!", "For Karl!", "Rock and Stone!"])
