from pydantic import BaseModel, EmailStr

class TriggerWorkflowIn(BaseModel):
    query: str


class TriggerWorkflowOut(BaseModel):
    query: str
