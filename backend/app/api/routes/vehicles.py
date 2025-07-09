import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path

from app.api.deps import SessionDep
from app.models.vehicle import *

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.post("/new")
async def create_vehicle(
    session: SessionDep,
    vehicle: VehicleCreate
):
    """
    Create a new vehicle
    """
    return

@router.get("/details/{vehicle_id}", response_model=VehiclePublic | VehiclePrivate)
async def get_vehicle_details(
    session: SessionDep,
    vehicle_id: uuid.UUID
):
    """
    Get vehicle details
    """
    raise HTTPException(
        403,
        "Forbidden"
        )

    return

@router.get("/list", response_model=Vehicles)
async def get_vehicle_list(
    session: SessionDep
):
    """
    Returns a list of all vehicles availabel to a user.
    """
    return

@router.patch("/details/update/{vehicle_id}")
async def update_vehicle_details(
    session: SessionDep,
    vehicle_id: uuid.UUID,
    vehicle: VehicleUpdate
):
    """
    Update vehicle details
    """
    return

@router.delete("/delete/{vehicle_id}")
async def delete_vehicle(
    session: SessionDep,
    vehicle_id: uuid.UUID
):
    """
    Delete a vehicle
    """
    return