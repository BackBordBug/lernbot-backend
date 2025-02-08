from fastapi import FastAPI, Request
import openai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Erlaubt Anfragen von überall (später kann das eingeschränkt werden)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI API-Schlüssel (später in einer sicheren Umgebung speichern)
OPENAI_API_KEY = "dein-api-schluessel"

@app.post("/chat")
async def chat_with_gpt(request: Request):
    data = await request.json()
    user_message = data.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}],
        api_key=OPENAI_API_KEY
    )

    return {"response": response["choices"][0]["message"]["content"]}

@app.get("/")
def home():
    return {"message": "Lernbot API läuft!"}
