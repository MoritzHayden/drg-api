from pydantic import BaseModel, Field


class Trivia(BaseModel):
    """
    A list of game trivia.
    """
    trivia: list[str] = Field(example=["Deep Dives were added in the September 26th, 2019 update.",
                                       "If you are falling at a height that would hurt you, and you fall on a fellow dwarf, you dont get hurt."])
