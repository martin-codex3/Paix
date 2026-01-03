from fastapi import FastAPI


app = FastAPI()

app.get("/")
async def root():
    return {"message": "we will start working here"}