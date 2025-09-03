from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def root():
    return "ok"

@app.post("/phones")
async def creation():
    return "null"



@app.get("/phones/{Id}")
async def say_hello(Id: int):
    return {"message": f"Hello {Id}"}
