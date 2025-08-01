import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, UploadFile, status

from app.api.deps import SessionDep, CurrentUser
from app.models.drive import *

router = APIRouter(prefix="/drives", tags=["Drives"])

@router.get("/list", response_model=DriveListPrivate)
async def list_drives(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Returns a list of all your drives.
    """
    # TODO
    return

@router.get("/list/{user_id}", response_model=DriveListPublic)
async def list_users_drives(
    session: SessionDep,
    current_user: CurrentUser,
    user_id: uuid.UUID
):
    """
    List another users public drives.
    """
    # TODO
    return


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_empty_drive(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Create an "empty" drive, without GPS data.
    """
    # TODO
    return

@router.post("/create/file", status_code=status.HTTP_201_CREATED)
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
    drive_id: uuid.UUID,
    file: UploadFile
):
    """
    Add a tracking file to an existing drive.
    """
    raise HTTPException(
        status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        detail="Unsupported file type."
    )
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

@router.get("/marker/{drive_id}")
async def get_drive_markers(
    session: SessionDep,
    current_user: CurrentUser,
    drive_id: uuid.UUID
):
    """
    Get all markers from a drive.
    """
    # TODO
    return

@router.post("/marker/{drive_id}")
async def add_marker(
    session: SessionDep,
    current_user: CurrentUser,
    drive_id: uuid.UUID
):
    """
    Add a marker to a drive.
    """
    # TODO
    return

@router.patch("/marker/{marker_id}")
async def edit_marker(
    session: SessionDep,
    current_user: CurrentUser,
    marker_id: uuid.UUID
):
    """
    Update a marker.
    """
    # TODO
    return

@router.delete("/marker/{marker_id}")
async def delete_marker(
    session: SessionDep,
    current_user: CurrentUser,
    marker_id: uuid.UUID
):
    """
    Delete a marker.
    """
    # TODO
    return

@router.post("/highlight")
async def highlight_track(
    session: SessionDep,
    current_user: CurrentUser
):
    """
    Pass a list of consecutive points to highlight.
    """
    # TODO
    return

@router.patch("/highlight/{highlight_id}")
async def edit_track_highlight(
    session: SessionDep,
    current_user: CurrentUser,
    data: MarkerUpdate
):
    """
    Edit information about highlight track segments.
    """
    # TODO
    return

@router.delete("/highlight/{highlight_id}")
async def delet_track_highlight(
    session: SessionDep,
    current_user: CurrentUser,
    highlight_id: uuid.UUID
):
    """
    Delete a highlight.
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
    # TODO
    return
