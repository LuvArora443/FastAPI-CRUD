from fastapi import APIRouter, HTTPException
from database import database
from bson import ObjectId

router = APIRouter()

@router.post("/posts/{post_id}/like")
async def like_post(post_id: str, liked: bool):
    post = database.posts.find_one({"_id": ObjectId(post_id)})
    if post:
        if post.get("liked") == liked:
            return {"message": f"Post {post_id} is already {'liked' if liked else 'unliked'}"}
        else:
            result = database.posts.update_one(
                {"_id": ObjectId(post_id)},
                {"$set": {"liked": liked}}
            )
            if result.modified_count == 1:
                return {"message": f"Post {post_id} {'liked' if liked else 'unliked'} successfully"}
            else:
                raise HTTPException(status_code=500, detail="Failed to update post")
    else:
        raise HTTPException(status_code=404, detail="Post not found")
