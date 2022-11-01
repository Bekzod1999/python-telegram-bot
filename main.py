import telegram
TOKEN='5749805943:AAHm17X_M1Sof1MZBCGT-cZE3dGYGxeSPfw'
bot = telegram.Bot(token=TOKEN)

imgUrl = 'https://c.ndtvimg.com/2020-08/h5mk7js_cat-generic_625x300_28_August_20.jpg'
img = open('allDocument\eagle.jpg', 'rb')
# document = open('allDocument\english.pdf', 'rb')
voiceUrl = 'https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3'
documentUrl = 'https://library.samdu.uz/files/edac813a68425234303341cd3a4ab787_Biologiya.pdf'
# video = open('allDocument\m.mp4', 'rb')
videoUrl = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4'


new_id = -1
while True:
    update = bot.getUpdates()[-1]
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    text = update.message.text.lower()

    #reply_markup 
    buttonVideo = {'text': 'Send video'}
    buttonVoice = {'text': 'Send voice'}
    buttonDocument = {'text': 'Send document'}
    buttonDice = {'text': 'Send Dice'}
    buttonPhoto = {'text': 'Send photo'}
    buttonMessage = {'text': 'Send message'}
    keyboard = [
        [buttonVideo, buttonVoice, buttonDocument],
        [buttonDice, buttonPhoto, buttonMessage]
    ]
    reply_markup = {
        'keyboard': keyboard,
        'resize_keyboard': True
    }

    #sendVideo
    if new_id != message_id and (text == 'send video' or text == 'video'):
        bot.sendVideo(chat_id, video=videoUrl, reply_markup = reply_markup)
        new_id = message_id
    #sendVoice
    elif new_id != message_id and (text == 'send voice' or text == 'voice'):
        bot.sendVoice(chat_id, voice=voiceUrl, reply_markup = reply_markup)
        new_id = message_id
    # sendDocument
    elif new_id != message_id and (text == 'send document' or text == 'document'):
        bot.sendDocument(chat_id, document = documentUrl, reply_markup = reply_markup)
        new_id = message_id

    #sendDice
    elif new_id != message_id and (text == 'send dice' or text == 'dice'):
        bot.sendDice(chat_id, reply_markup = reply_markup)
        new_id = message_id

    #sendPhoto
    elif new_id != message_id and (text == 'send photo' or text == 'photo'):
        bot.sendPhoto(chat_id, photo = imgUrl, reply_markup = reply_markup)
        new_id = message_id

    #sendMessage
    elif new_id != message_id:
        bot.sendMessage(chat_id, text, reply_markup = reply_markup)
        new_id = message_id