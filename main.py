from fastapi import FastAPI
from typing import Dict

# Initialize the FastAPI app
app = FastAPI(
    title="My Azure FastAPI App",
    description="A simple API deployed for free on Azure",
    version="1.0.0"
)

@app.get("/")
def read_root() -> Dict[str, str]:
    """
    Landing page for the API.
    """
    return {
        "message": "Welcome to your FastAPI app on Azure!",
        "status": "Online",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """
    Endpoint for Azure to monitor app health.
    """
    return {"status": "healthy"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    Example of a path parameter and a query parameter.
    """
    return {"item_id": item_id, "query_param": q}