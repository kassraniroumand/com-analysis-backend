from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class IdeaStatus(str, Enum):
    NEW = "new"
    PROCESSING = "processing"
    COMPLETED = "completed"


class SortOrder(str, Enum):
    NEWEST_FIRST = "newest_first"
    OLDEST_FIRST = "oldest_first"


class IdeaRequest(BaseModel):
    idea: str
    target_audience: str
    marketIndustry: str
    geography: str
    business_model: str
    keywords: list[str] = []


class IdeaResponse(BaseModel):
    task_id: str


class IdeasDashboardStats(BaseModel):
    total_ideas: int
    completed: int
    processing: int
    avg_score: Optional[float] = None


class IdeaSummary(BaseModel):
    id: int
    title: str
    description: str
    category: str
    status: IdeaStatus = IdeaStatus.PROCESSING
    score: Optional[int] = Field(None, ge=0, le=100)
    tags: list[str] = []
    created_at: date


class IdeasFilter(BaseModel):
    search: Optional[str] = None
    status: Optional[IdeaStatus] = None
    sort: SortOrder = SortOrder.NEWEST_FIRST


class IdeasListResponse(BaseModel):
    ideas: list[IdeaSummary]
    total: int