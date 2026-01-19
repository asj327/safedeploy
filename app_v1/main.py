from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SafeDeploy App v1"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/api")
def api():
    return {"response": "Hello from v1"}
