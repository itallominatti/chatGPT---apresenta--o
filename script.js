const chatMessages = document.getElementById('chat-messages');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', enviarMensagem);

function enviarMensagem() {
  const messageContent = messageInput.value;

  fetch('/envia_mensagem', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ content: messageContent }),
  })
    .then((response) => response.json())
    .then((data) => {
      exibirMensagemEnviada(messageContent);
      messageInput.value = '';
    })
    .catch((error) => {
      console.error('Erro:', error);
    });
}

function exibirMensagemEnviada(messageContent) {
  const messageElement = document.createElement('div');
  messageElement.classList.add('message', 'sent');
  messageElement.textContent = `Eu: ${messageContent}`;
  chatMessages.appendChild(messageElement);
  scrollToBottom();
}

function scrollToBottom() {
  chatMessages.scrollTop = chatMessages.scrollHeight;
}
