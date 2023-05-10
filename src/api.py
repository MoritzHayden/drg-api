from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from model.deepdives import DeepDives
from util.constants import (
    API_TITLE,
    API_DESCRIPTION,
    API_VERSION,
    API_LICENSE_NAME,
    API_ROOT,
    CONTACT_NAME,
    CONTACT_EMAIL,
    GITHUB_TOS_URL,
    GITHUB_LICENSE_URL,
    DEEPDIVES_PATH,
    FAVICON_PATH,
    NAME,
    URL,
    EMAIL,
)


# Initialize FastAPI
api = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
    docs_url=API_ROOT,
    terms_of_service=GITHUB_TOS_URL,
    contact={
        NAME: CONTACT_NAME,
        EMAIL: CONTACT_EMAIL,
    },
    license_info={
        NAME: API_LICENSE_NAME,
        URL: GITHUB_LICENSE_URL,
    },
    swagger_favicon_url=FAVICON_PATH
)


# Deep Dives
@api.get("/deepdives", tags=["v1"], response_model=DeepDives, status_code=200)
async def deepdives() -> DeepDives:
    """
    Get the weekly Deep Dive details.
    """
    with open(DEEPDIVES_PATH, "r") as file:
        return DeepDives.parse_raw(file.read())


# Health Check
@api.get("/health", tags=["v1"], response_class=JSONResponse, status_code=200)
async def health() -> dict:
    """
    Check the health status of the API.
    """
    return {}


# Favicon
@api.get('/favicon.ico', response_class=FileResponse, include_in_schema=False)
async def favicon():
    """
    Get the favicon for the API.
    """
    return FileResponse(FAVICON_PATH)
