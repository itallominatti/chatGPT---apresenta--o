from fastapi import FastAPI
from pydantic import BaseModel
from main import ChatGPT
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    content: str

chat_gpt = ChatGPT()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/envia_mensagem")
def envia_mensagem(message: Message):
    chat_gpt.send_message(message.content)
    return Response(content={"message": "Mensagem enviada"})

@app.get("/conecta_openai")
def conecta_openai():
    chat_gpt.Conecta_openai()
    return {"message": "Conexão estabelecida com a OpenAI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3030)
