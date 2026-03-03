from fastapi import FastAPI

app = FastAPI(title="Real Estate Intelligence Engine")

@app.get("/")
def root():
    return {"message": "Real Estate Intelligence Engine is running"}