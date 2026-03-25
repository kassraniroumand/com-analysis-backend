from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from authentication.router import router as auth_router
from workflow.router import router as workflow_router

app = FastAPI(title="Com Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(workflow_router)


@app.get("/api/health")
async def health():
    return {"status": "ok 4"}
