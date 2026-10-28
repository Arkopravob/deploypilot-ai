from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "deploymentAI!"}

@app.get("/ui",responses_class=HTMLResponse)
def ui():
    return """
    <h1>DeployPilot AI </h1>
    <h2>Ai running on deployment env </h2>
    <p>status: Live </p>
    """
