from fastapi import APIRouter, HTTPException, Depends
from pymongo.collection import Collection
from database import database
from models import Post
from crud import create_post, get_posts, update_post, delete_post

router = APIRouter()

@router.post("/posts/")
async def create_new_post(post: Post):
    result = create_post(post, database.posts)
    return {"message": "Post created successfully", "post_id": str(result.inserted_id)}

@router.get("/posts/")
async def get_all_posts():
    posts = get_posts(database.posts)
    return posts

@router.put("/posts/{post_id}")
async def update_existing_post(post_id: str, updated_post: Post):
    result = update_post(post_id, updated_post, database.posts)
    if result.modified_count == 1:
        return {"message": "Post updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@router.delete("/posts/{post_id}")
async def delete_existing_post(post_id: str):
    result = delete_post(post_id, database.posts)
    if result.deleted_count == 1:
        return {"message": "Post deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
    


