from fastapi import FastAPI

from app.routes.postRoutes import router as postRouter
from app.routes.userRoutes import router as userRouter


app = FastAPI()


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your blog!."}


# include other routers
app.include_router(postRouter)
app.include_router(userRouter)
