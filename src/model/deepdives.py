from pydantic import BaseModel
from typing import Optional


class Stage(BaseModel):
    id: int
    primary: str
    secondary: str
    anomaly: Optional[str] = None
    warning: Optional[str] = None

class Variant(BaseModel):
    variant: str
    name: str
    biome: str
    seed: int
    stages: list[Stage]

class DeepDives(BaseModel):
    startTime: str
    endTime: str
    variants: list[Variant]
