from datetime import date

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .authentication.router import router as auth_router
from .schemas.req_res_types import (
    IdeaStatus, IdeaSummary, IdeasDashboardStats, IdeasListResponse,
)
from .workflow.router import router as workflow_router

app = FastAPI(title="Com Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(workflow_router)
idea_router = APIRouter(prefix="/api/v1/ideas", tags=["ideas"])


@app.get("/api/health")
async def health():
    return {"status": "ok 6"}


@idea_router.get("/list", response_model=IdeasListResponse)
async def get_ideas():
    idea_list_summery = [
        IdeaSummary(
            id=1,
            title="Idea 1",
            description="Description of Idea 1",
            category="Tech",
            status=IdeaStatus.NEW,
            score=85,
            tags=["AI", "ML"],
            created_at=date(2024, 6, 1)
        ),
        IdeaSummary(
            id=2,
            title="Idea 2",
            description="Description of Idea 2",
            category="Business",
            status=IdeaStatus.PROCESSING,
            score=43,
            tags=["Finance", "Marketing"],
            created_at=date(2024, 6, 2)
        ),
        IdeaSummary(
            id=3,
            title="Idea 3",
            description="Description of Idea 2",
            category="Business",
            status=IdeaStatus.PROCESSING,
            score=43,
            tags=["Finance", "Marketing"],
            created_at=date(2024, 6, 2)
        )
    ]
    return IdeasListResponse(
        ideas=idea_list_summery,
        total=len(idea_list_summery),
    )


@idea_router.get("/stat", response_model=IdeasDashboardStats)
async def get_ideas_stats():
    return IdeasDashboardStats(
        total_ideas=2,
        completed=1,
        processing=1,
        avg_score=85
    )


app.include_router(idea_router)