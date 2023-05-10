from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
from .model.deepdives import DeepDives
from .model.salutes import Salutes
from .model.trivia import Trivia
from core.util.constants import V1_DEEPDIVES_PATH, V1_SALUTES_PATH, V1_TRIVIA_PATH


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
    with open(V1_DEEPDIVES_PATH, "r") as file:
        return DeepDives.parse_raw(file.read())


# Salutes
@router.get(path="/salutes", name="Salutes", response_model=Salutes, status_code=200)
async def salutes():
    """
    Get a list of salutes used in the game.
    """
    with open(V1_SALUTES_PATH, "r") as file:
        return Salutes.parse_raw(file.read())


# Trivia
@router.get(path="/trivia", name="Trivia", response_model=Trivia, status_code=200)
async def trivia() -> Trivia:
    """
    Get a list of game trivia.
    """
    with open(V1_TRIVIA_PATH, "r") as file:
        return Trivia.parse_raw(file.read())
