from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from core.util.constants import (
    API_TITLE,
    API_DESCRIPTION,
    API_VERSION,
    API_LICENSE_NAME,
    CONTACT_NAME,
    CONTACT_EMAIL,
    GITHUB_TOS_URL,
    GITHUB_LICENSE_URL,
    FAVICON_PATH,
    FAVICON_URL,
    OPEN_API_URL,
    NAME,
    URL,
    EMAIL
)
from v1.api import router as v1_router


# Initialize FastAPI
api = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
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


# Add Routers
api.include_router(v1_router)


# Swagger UI HTML
@api.get("/", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        title=API_TITLE,
        openapi_url=OPEN_API_URL,
        swagger_favicon_url=FAVICON_URL
    )


# Health
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
