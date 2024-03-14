# Beginning of app.py
from fastapi import FastAPI

app = FastAPI()

# "uvicorn main:app --reload" may not work
# Use: "python -m uvicorn main:app --reload" instead 
# Make sure you're in the PATIENT_SERVICE_API folder, and not any deeper

# Create a virtual environment with "python -m venv env" 

# After starting the virtual environment, activate it in bash with: 
'''
$ cd env/Scripts/
$ . activate  OR $ .[backslash]activate
'''

@app.get("/")
async def root():
    return {"message": "Hello World"} 

@app.get("/users")
async def getUsers():
    return [
    {
        "firstName": "Some", 
        "lastName": "One", 
        "email": "someone@gmail.com"
        
    } 
    ] 