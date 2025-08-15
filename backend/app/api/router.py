from fastapi import APIRouter

from app.api.routes import users, auth, friends, vehicles, drives, dev
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(auth.router)
api_router.include_router(friends.router)
api_router.include_router(vehicles.router)
api_router.include_router(drives.router)

# If the environemt variable ENVIRONMENT is set to "dev" load development route.
if settings.ENVIRONMENT == "dev":
    api_router.include_router(dev.dev_router)
