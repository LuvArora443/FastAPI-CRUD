from fastapi import FastAPI
from routers import blog, comment,like

app = FastAPI()

app.include_router(blog.router)
app.include_router(comment.router)
app.include_router(like.router)
