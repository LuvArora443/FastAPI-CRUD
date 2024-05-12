from fastapi import APIRouter, HTTPException
from database import database
from models import Comment
from crud import create_comment, get_comment, update_comment, delete_comment

router = APIRouter()

@router.post("/posts/{post_id}/comments/")
async def create_new_comment(post_id: str, comment: Comment):
    result = create_comment(post_id, comment, database.comments)
    return {"message": "Comment created successfully", "comment_id": str(result.inserted_id)}

@router.get("/posts/{post_id}/comments/{comment_id}")
async def get_single_comment(comment_id: str):
    comment = get_comment(comment_id, database.comments)
    if comment:
        return comment
    else:
        raise HTTPException(status_code=404, detail="Comment not found")

@router.put("/posts/{post_id}/comments/{comment_id}")
async def update_existing_comment( comment_id: str, updated_comment: Comment):
    existing_comment = get_comment(comment_id, database.comments)
    
    if existing_comment:
        if existing_comment != updated_comment.dict():
            result = update_comment(comment_id, updated_comment, database.comments)
            if result.modified_count == 1:
                return {"message": "Comment updated successfully"}
            else:
                raise HTTPException(status_code=500, detail="Failed to update comment")
        else:
            return {"message": "Comment unchanged"}
    else:
        raise HTTPException(status_code=404, detail="Comment not found")


@router.delete("/posts/{post_id}/comments/{comment_id}")
async def delete_existing_comment(comment_id: str):
    result = delete_comment(comment_id, database.comments)
    if result.deleted_count == 1:
        return {"message": "Comment deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Comment not found")
