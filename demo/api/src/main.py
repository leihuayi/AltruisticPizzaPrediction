import shutil, os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from raopred import predict

app = FastAPI()

origins = [
    "http://raopred.l4th.fr",
    "https://raopred.l4th.fr",
    "http://localhost",
    "http://localhost:8080",
]

# allow requests from front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=PlainTextResponse)
def home():
    return "RAOP API"


@app.post("/upload")
async def predict(req : Request):
    data = await req.json()
    print(data)

    input_data = [
        data["title"] + ' ' + data["text"],
        len(data["text"]),
        data["num_downvotes"],
        data["num_upvotes"],
        data["num_comments"]
    ]

    #label = predict(input_data)
    label=False
    return {"label": label}
