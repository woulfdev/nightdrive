from fastapi import APIRouter

from app.api.routes import users, auth, friends, vehicle

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(auth.router)
api_router.include_router(friends.router)
api_router.include_router(vehicle.router)
