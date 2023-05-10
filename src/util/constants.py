from pydantic import Field

# Contact
CONTACT_NAME: str = "DRG API Help"
CONTACT_EMAIL: str = "help@drgapi.com"

# GitHub
GITHUB_ROOT_URL: str = "https://github.com/MoritzHayden/drg-api"
GITHUB_LICENSE_URL: str = "/".join([GITHUB_ROOT_URL, "blob", "main", "LICENSE"])
GITHUB_TOS_URL: str = "/".join([GITHUB_ROOT_URL, "blob", "main", "docs", "TERMS-OF-SERVICE.md"])

# API
API_TITLE: str = "DRG API"
API_DESCRIPTION: str = f"""
DRG API is a free API which returns Deep Rock Galactic information and resources.

View the source code on [GitHub]({GITHUB_ROOT_URL}).
"""
API_VERSION: str = "1.0.0"
API_LICENSE_NAME: str = "MIT License"
API_ROOT: str = "/"

# Paths
DEEPDIVES_PATH: str = "json/deepdives.json"
FAVICON_PATH: str = "favicon.ico"

# Misc
NAME: str = "name"
URL: str = "url"
EMAIL: str = "email"
