from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SafeDeploy App v2 (canary)"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/api")
def api():
    # Simulated bug
    raise Exception("Something went wrong in v2!")  


