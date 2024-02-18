from fastapi import APIRouter

router = APIRouter()


@router.get("/get_score")
async def get_score():
    return {"option1": "score1", "option2": "score2", "option3": "score3"}
