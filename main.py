from email import message
import telegram
TOKEN='5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'
bot = telegram.Bot(token=TOKEN)

imgNet = 'https://c.ndtvimg.com/2020-08/h5mk7js_cat-generic_625x300_28_August_20.jpg'
img = open('allDocument\eagle.jpg', 'rb')
document = open('allDocument\english.pdf', 'rb')
video = open('allDocument\m.mp4', 'rb')
videoUrl = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4'


new_id = -1
while True:
    update = bot.getUpdates()[-1]
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    text = update.message.text.lower()

    #sendVideo
    if new_id != message_id and text == 'send video':
        bot.sendVideo(chat_id, video=videoUrl)
        new_id = message_id

    # sendDocument
    if new_id != message_id and text == 'send document':
        bot.sendDocument(chat_id, document = document)
        new_id = message_id

    #sendDice
    elif new_id != message_id and text == 'send dice':
        bot.sendDice(chat_id)
        new_id = message_id

    #sendPhoto
    elif new_id != message_id and text == 'send photo':
        bot.sendPhoto(chat_id, photo = img)
        new_id = message_id

    #sendMessage
    elif new_id != message_id:
        bot.sendMessage(chat_id, text)
        new_id = message_id