from fastapi import APIRouter, Depends, HTTPException, status


from .models import TriggerWorkflowIn, TriggerWorkflowOut

router = APIRouter(prefix="/api/workflow", tags=["workflow"])

@router.post("/trigger", response_model=TriggerWorkflowOut)
async def register(data: TriggerWorkflowIn):
    print(data.query)
    return TriggerWorkflowOut(query="query")

