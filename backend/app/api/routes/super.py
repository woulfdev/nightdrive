from fastapi import APIRouter

sub_router = APIRouter(
    prefix="/super",
    tags=["Superuser"]
)

@sub_router.post("/password/reset")
async def reset_user_password():
    """
    Allows administrators to reset a users password.
    """
    return