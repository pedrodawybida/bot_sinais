import os
from telethon import TelegramClient, events

sessao = 'repassar_mensagem'
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

def alterar_titulo(mensagem, novo_titulo):
    linhas = mensagem.split('\n')
    linhas[0] = novo_titulo
    return '\n'.join(linhas)

async def enviar_mensagem(event, client):
    mensagem = event.raw_text
    linhas = mensagem.split('\n')

    if linhas[0].startswith("📊SALA VIP | Mateus Trader📊"):
        if len(linhas) > 1 and linhas[1].startswith("🔔 Resultados para o dia"):
            return
        
        nova_mensagem = alterar_titulo(mensagem, "📊SALA VIP📊")
        await client.send_message(4587247538, nova_mensagem)

def main():
    client = TelegramClient(sessao, api_id, api_hash)

    @client.on(events.NewMessage(chats=[4507534222]))
    async def handler(event):
        await enviar_mensagem(event, client)

    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
