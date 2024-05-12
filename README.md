# FastAPI CRUD with MongoDB

This FastAPI application provides CRUD (Create, Read, Update, Delete) operations for managing posts and comments, using MongoDB as the database. Users can perform various actions such as creating, updating, and deleting posts, as well as adding comments to posts and interacting with them.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Features

- **Create Post:** Users can create a new post with title, content, etc.
- **Read Post:** Retrieve all posts or a single post by its ID.
- **Update Post:** Modify an existing post with new data.
- **Delete Post:** Remove a post from the database.
- **Create Comment:** Add comments to posts.
- **Read Comment:** View comments on a post.
- **Update Comment:** Modify an existing comment.
- **Delete Comment:** Remove a comment from a post.
- **Like/Dislike Post:** Allow users to like or dislike a post.

## Endpoints

- **POST /posts/:** Create a new post.
- **GET /posts/:** Retrieve all posts.
- **GET /posts/{post_id}:** Retrieve a single post by ID.
- **PUT /posts/{post_id}:** Update an existing post.
- **DELETE /posts/{post_id}:** Delete a post.
- **POST /posts/{post_id}/comments/:** Add a comment to a post.
- **GET /posts/{post_id}/comments/{comment_id}:** Retrieve a single comment on a post.
- **PUT /posts/{post_id}/comments/{comment_id}:** Update a comment on a post.
- **DELETE /posts/{post_id}/comments/{comment_id}:** Delete a comment on a post.
- **POST /posts/{post_id}/like:** Like or dislike a post.

## Usage

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Access the API endpoints on /docs route

