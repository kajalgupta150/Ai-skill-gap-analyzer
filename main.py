from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    skills: list[str]
    target_role: str

@app.post("/analyze")
def analyze_skill_gap(data: AnalyzeRequest):
    missing_skills = ["Docker", "System Design", "AWS"]

    return {
        "current_skills": data.skills,
        "target_role": data.target_role,
        "missing_skills": missing_skills
    }
