from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from core.util.constants import (
    API_TITLE,
    API_DESCRIPTION,
    API_VERSION,
    API_LICENSE_NAME,
    API_ROOT,
    CONTACT_NAME,
    CONTACT_EMAIL,
    GITHUB_TOS_URL,
    GITHUB_LICENSE_URL,
    FAVICON_PATH,
    NAME,
    URL,
    EMAIL,
)
import v1.api as v1


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
)


# Add Routers
api.include_router(v1.router)


# Health Check
@api.get(path="/health", name="Health", tags=["default"], response_class=JSONResponse, status_code=200)
async def health() -> dict:
    """
    Check the health of the API.
    """
    return {}


# Favicon
@api.get(path='/favicon.ico', name="Favicon", tags=["default"], response_class=FileResponse, include_in_schema=False)
async def favicon():
    """
    Get the favicon for the API.
    """
    return FileResponse(FAVICON_PATH)
