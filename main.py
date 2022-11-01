import telegram
TOKEN='5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'
bot = telegram.Bot(token=TOKEN)

#sendMessage

new_id = -1
while True:
    update = bot.getUpdates()[-1]
    chat_id = update['message']['chat']['id']
    message_id = update['message']['message_id']
    text = update['message']['text']

    if new_id != message_id:
        bot.sendMessage(chat_id, text)
        new_id = message_id
