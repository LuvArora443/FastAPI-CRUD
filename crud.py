from pymongo.collection import Collection
from models import Post, Comment
from bson import ObjectId
import logging

logger = logging.getLogger(__name__)


def create_post(post: Post, collection: Collection):
    return collection.insert_one(post.dict())

def get_posts(collection: Collection):
    posts = list(collection.find())
    return [{**post, '_id': str(post['_id'])} for post in posts]

def update_post(post_id: str, updated_post: Post, collection: Collection):
    post_id_obj = ObjectId(post_id)
    return collection.update_one({"_id": post_id_obj}, {"$set": updated_post.dict()})

def delete_post(post_id: str, collection: Collection):
    post_id_obj = ObjectId(post_id)
    return collection.delete_one({"_id": post_id_obj})

def create_comment(post_id: str, comment: Comment, collection: Collection):
    comment_dict = comment.dict()
    comment_dict['post_id'] = post_id
    return collection.insert_one(comment_dict)

def get_comment(comment_id: str, collection: Collection):
    comment_id = ObjectId(comment_id)
    comment = collection.find_one({"_id": comment_id})
    return {**comment, '_id': str(comment['_id'])} if comment else None

def update_comment(comment_id: str, updated_comment: Comment, collection: Collection):
    return collection.update_one({"_id": ObjectId(comment_id)}, {"$set": updated_comment.dict()})

def delete_comment(comment_id: str, collection: Collection):
    return collection.delete_one({"_id": ObjectId(comment_id)})

def like_post(post_id: str, liked: bool, collection: Collection):
    return collection.update_one({"_id": ObjectId(post_id)}, {"$set": {"liked" : liked}})

