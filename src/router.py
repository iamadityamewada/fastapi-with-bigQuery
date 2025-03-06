from fastapi import APIRouter
from src.experimentDTO import ExperimentDTO
# from src.services import experiment_services


router = APIRouter(prefix="/api/v1")



@router.post("/experiment/")
async def create_experiment(data: ExperimentDTO):
    return {"message": "Experiment created successfully!", "data": data}


