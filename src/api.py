from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from model.deepdives import DeepDives
from util.constants import (
    API_TITLE,
    API_DESCRIPTION,
    API_VERSION,
    API_LICENSE_NAME,
    CONTACT_NAME,
    CONTACT_EMAIL,
    DOMAIN_TOS_URL,
    DOMAIN_LICENSE_URL,
    GITHUB_ROOT_URL,
    GITHUB_LICENSE_URL,
    GITHUB_TOS_URL,
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
    terms_of_service=DOMAIN_TOS_URL,
    contact={
        NAME: CONTACT_NAME,
        EMAIL: CONTACT_EMAIL,
    },
    license_info={
        NAME: API_LICENSE_NAME,
        URL: DOMAIN_LICENSE_URL,
    },
)

# Root Redirect
@api.get("/", response_class=RedirectResponse, status_code=301)
async def root() -> str:
    return GITHUB_ROOT_URL

# Deep Dives
@api.get("/deepdives", response_model=DeepDives, status_code=200)
async def deepdives() -> DeepDives:
    with open("json/deepdives.json", "r") as file:
        return DeepDives.parse_raw(file.read())

# Terms of Service
@api.get("/tos", response_class=RedirectResponse, status_code=301)
async def tos() -> dict:
    return GITHUB_TOS_URL

# License
@api.get("/license", response_class=RedirectResponse, status_code=301)
async def license() -> dict:
    return GITHUB_LICENSE_URL

# Health Check
@api.get("/health", response_class=JSONResponse, status_code=200)
async def health() -> dict:
    return {STATUS: OK}
