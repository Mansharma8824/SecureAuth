from fastapi import FastAPI

app = FastAPI(
    title= 'SecureAuth',
    description= 'Authontication and Authorization System',
    version= '0.1.0'
)

@app.get('/')
def root():
    return {
        "message": "Welcome to SecureAuth",
        "status": "running",
    }
    
@app.get('/health')
def helth_check():
    return {
        "status":"healthy",
    }