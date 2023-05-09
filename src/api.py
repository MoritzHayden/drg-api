from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
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
    DEEPDIVES_JSON,
    STATUS,
    OK,
    NAME,
    URL,
    EMAIL
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
    }
)

# Deep Dives
@api.get("/deepdives", response_model=DeepDives, status_code=200)
async def deepdives() -> DeepDives:
    with open(DEEPDIVES_JSON, "r") as file:
        return DeepDives.parse_raw(file.read())

# Health Check
@api.get("/health", response_class=JSONResponse, status_code=200)
async def health() -> dict:
    return {STATUS: OK}
