from fastapi import APIRouter

router = APIRouter()


@router.get("/platform/{portal_id}")
def access_portal(portal_id: int):
    return {"message": "Welcome"}
