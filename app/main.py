from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "deploymentAI!"}

@app.get("/health")
def health_check():
    return {"status": "running ok"}