from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/bfhl")
async def get_bfhl():
    return {"operation_code": 1}

@app.post("/bfhl")
async def post_bfhl(data: dict):
    numbers = [x for x in data['data'] if x.isdigit()]
    alphabets = [x for x in data['data'] if x.isalpha()]
    lowercase = [x for x in alphabets if x.islower()]
    highest_lowercase = max(lowercase) if lowercase else None
    return {
        "is_success": True,
        "user_id": "kartheekvardhanyakkala_22082003",
        "email": "kartheek.21bce7085@vitapstudent.ac.in",
        "roll_number": "21BCE7085",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase
    }
