from fastapi import FastAPI
from databases import Database

# Replace 'notebot1' and 'notebot1' with your username and password
DATABASE_URL = "postgresql://notebot1:notebot1@localhost/notebot"

database = Database(DATABASE_URL)
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def read_root():
    return {"message": "Connected to PostgreSQL!"}
