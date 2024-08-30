from telethon import TelegramClient, events
import senhas

sessao = 'repassar_mensagem'

def alterar_titulo(mensagem, novo_titulo):
    # Separa a mensagem em linhas
    linhas = mensagem.split('\n')
    
    # Substitui a primeira linha (título) pelo novo título
    linhas[0] = novo_titulo
    
    # Reune as linhas de volta em uma string
    nova_mensagem = '\n'.join(linhas)
    
    return nova_mensagem

def main():
    client = TelegramClient(sessao, senhas.api_id, senhas.api_hash)

    @client.on(events.NewMessage(chats=[4507534222]))
    async def enviar_mensagem(event):
        mensagem = event.raw_text
        
        # Verifica se a mensagem contém o título que você deseja modificar
        if mensagem.startswith("📊SALA VIP | Mateus Trader📊"):
            # Altera o título para "SALA VIP"
            nova_mensagem = alterar_titulo(mensagem, "SALA VIP")
            
            # Envia a mensagem alterada para o outro chat
            await client.send_message(4587247538, nova_mensagem)
        else:
            # Caso não seja a mensagem alvo, repassa sem alterações
            await client.send_message(4587247538, mensagem)

    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
