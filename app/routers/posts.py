from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, utils
from ..dependencies import get_current_user
from typing import List

router = APIRouter()

@router.post("/add_post")
def add_post(
    post_in: schemas.PostCreate,
    current_user: schemas.UserCreate = Depends(get_current_user)
):
    if not utils.validate_payload_size(post_in.text):
        raise HTTPException(status_code=400, detail="Payload too large (max 1MB)")
    post_id = utils.add_post_to_store(current_user.email, post_in.text)
    return {"post_id": post_id}

@router.get("/get_posts", response_model=List[schemas.PostOut])
def get_posts(current_user: schemas.UserCreate = Depends(get_current_user)):
    return utils.get_posts_for_user(current_user.email)

@router.delete("/delete_post/{post_id}")
def delete_post(post_id: str, current_user: schemas.UserCreate = Depends(get_current_user)):
    success = utils.delete_post(current_user.email, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found or unauthorized")
    return {"status": "deleted"}

