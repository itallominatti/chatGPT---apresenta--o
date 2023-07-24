import time
import requests
import json

from settings import API_KEY, LINK_OPENAI, LINK_GPT, ID_MODELO


class ChatGPT:
    def __init__(self):
        self.key = API_KEY
        self.link = LINK_OPENAI
        self.headers = {
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json"
        }
        self.last_request_time = time.time()

    def connect_openai(self):
        resposta = requests.get(self.link, headers=self.headers)
        self.resposta = resposta
        print(self.resposta.text)
        return resposta

    def send_message(self):
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < 2:
            time.sleep(2 - time_since_last_request)

        message_body = {
            "model": ID_MODELO,
            "messages": [{"role": "user", "content": "qual a data de nascimento de barack obama?"}]
        }
        message_body = json.dumps(message_body)

        response = requests.post(LINK_GPT, headers=self.headers, data=message_body)

        if response.status_code == 200:
            self.last_request_time = time.time()
            response_data = response.json()
            message = response_data["choices"][0]["message"]["content"]
            print(message)
            
        elif response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 5))
            print(f"Erro 429 - Muitas requisições. Tentando novamente em {retry_after} segundos...")
            time.sleep(retry_after)
            self.send_message()
            
        else:
            print("Algum erro ocorreu na chamada da API pela OpenAI.")


if __name__ == "__main__":
    chatbot = ChatGPT()
    chatbot.connect_openai()
   
