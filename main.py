from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from api.api import router  
import yaml


app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

def custom_openapi():
    with open("openapi.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
    
app.openapi = custom_openapi


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "detail": str(exc)}
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

@app.get("/cause_error")
async def cause_error():
    raise HTTPException(status_code=400, detail="This is a test error message")

