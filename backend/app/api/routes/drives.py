import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, UploadFile

from app.api.deps import SessionDep, CurrentUser
from app.models.drive import *

router = APIRouter(prefix="/drives", tags=["Drives"])

@router.get("/list", response_model=DriveListPrivate)
async def list_drives(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Returns a list of all your drives
    """
    # TODO
    return

@router.get("", response_model=DriveListPublic)
async def list_users_drives(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    List another users public drives.
    """
    # TODO
    return


@router.post("/create")
async def create_empty_drive(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Create an "empty" drive, without GPS data.
    """
    # TODO
    return

@router.post("/create/file")
async def create_drive(
    session: SessionDep,
    current_user: CurrentUser,
    file: UploadFile
):
    """
    Create drive with tracking file.
    """
    # TODO
    return

@router.patch("/track/add/{drive_id}")
async def add_tracking_file(
    session: SessionDep,
    current_user: CurrentUser,
    drive_id: uuid.UUID
):
    """
    Add a tracking file to an existing drive.
    """
    # TODO
    return

@router.patch("/update")
async def upate_info(
    session:SessionDep,
    current_user: CurrentUser,
    data: DriveUpdate
):
    """
    Update drive data like name and description.
    """
    # TODO
    return

@router.delete("/delete/{drive_id}")
async def delete_drive(
        session: SessionDep,
        current_user: CurrentUser
):
    """
    Deletes a specific drive.
    """
    return
