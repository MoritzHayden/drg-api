from fastapi import APIRouter
from .model.deep_dives import DeepDives
from .model.salutes import Salutes
from .model.trivia import Trivia


# Initialize Routers
router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

# Deep Dives
@router.get(path="/deepdives", name="Deep Dives", response_model=DeepDives, status_code=200)
async def deepdives() -> DeepDives:
    """
    Get the current weekly Deep Dive details.
    """
    with open(file="v1/json/deep_dives.json", mode="r", encoding="UTF-8") as file:
        return DeepDives.parse_raw(file.read())


# Salutes
@router.get(path="/salutes", name="Salutes", response_model=Salutes, status_code=200)
async def salutes():
    """
    Get a list of salutes used in the game.
    """
    with open(file="v1/json/salutes.json", mode="r", encoding="UTF-8") as file:
        return Salutes.parse_raw(file.read())


# Trivia
@router.get(path="/trivia", name="Trivia", response_model=Trivia, status_code=200)
async def trivia() -> Trivia:
    """
    Get a list of game trivia.
    """
    with open(file="v1/json/trivia.json", mode="r", encoding="UTF-8") as file:
        return Trivia.parse_raw(file.read())
