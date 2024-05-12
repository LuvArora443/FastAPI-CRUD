from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    author: str

class Comment(BaseModel):
    text: str
    author: str

