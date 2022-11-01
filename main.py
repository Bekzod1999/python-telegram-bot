from email import message
import telegram
TOKEN='5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'
bot = telegram.Bot(token=TOKEN)

new_id = -1
while True:
    update = bot.getUpdates()[-1]
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    text = update.message.text.lower()

    # sendPhoto
    imgNet = 'https://c.ndtvimg.com/2020-08/h5mk7js_cat-generic_625x300_28_August_20.jpg'
    img = open('eagle.jpg', 'rb')
    if new_id != message_id and text == 'send photo':
        bot.sendPhoto(chat_id, photo = img)
        new_id = message_id

    #sendMessage
    elif new_id != message_id:
        bot.sendMessage(chat_id, text)
        new_id = message_id