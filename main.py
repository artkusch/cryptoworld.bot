import telebot
from telebot import types

bot = telebot.TeleBot('2118149675:AAEu0SgDutSRRWYC3Otylb83S2hsKJ55QXw')

admins = {'333835720', '1175647329'}
joinedUsers = set()
Subnft = set()
Subido = set()
Subfree_nft = set()
Subairdrop = set()


@bot.message_handler(commands=['start'])
def welcome(message):
    joinedFile = open("static1/Notif_id/rasslika.txt", "r")
    for line in joinedFile.readlines():
        joinedUsers.add(line.strip())
    joinedFile.close()
    print(5)
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("static1/Notif_id/rasslika.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(str(message.chat.id))

    sti = open('static1/pic/welocome.png', 'rb')
    # всплывающая клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup2 = types.InlineKeyboardMarkup()
    nft = types.KeyboardButton("🖼 NFT")
    ido = types.KeyboardButton("🪙 IDO/IFO")
    airdrop = types.KeyboardButton("🚀 AirDrop")
    free = types.KeyboardButton("🆓 Free NFT")
    sub = types.InlineKeyboardButton('Проверить подписку 🔄', callback_data='like')
    chanel = types.InlineKeyboardButton(text="ПОДПИСАТЬСЯ ✅", url="https://t.me/joinchat/Hp9mqusJHrIxYzUy")


    markup.add(nft, ido, airdrop, free)
    markup2.add(chanel,sub)

    #приветсвие
    user_status = bot.get_chat_member(chat_id='-1001705740568', user_id=message.from_user.id)
    # приветсвие
    print(user_status.status)
    if user_status.status == 'member' or user_status.status == 'creator' or user_status.status == 'administrator':
        bot.send_photo(message.from_user.id, sti)
        bot.send_message(message.from_user.id,"Привет, {0.first_name}!👋\nЯ - {1.first_name}, меня создали, чтобы я напоминал о важных событиях в криптомире.🌎".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id,"✉️ Для продолжения пользования ботом, пожалуйста, подпишитесь на наш канал.\n", parse_mode='html', reply_markup=markup2)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    markup2 = types.InlineKeyboardMarkup()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    sub = types.InlineKeyboardButton('Проверить подписку 🔄', callback_data='like')
    chanel = types.InlineKeyboardButton(text="ПОДПИСАТЬСЯ ✅", url="https://t.me/joinchat/Hp9mqusJHrIxYzUy")

    nft = types.KeyboardButton("🖼 NFT")
    ido = types.KeyboardButton("🪙 IDO/IFO")
    airdrop = types.KeyboardButton("🚀 AirDrop")
    free = types.KeyboardButton("🆓 Free NFT")

    markup2.add(chanel, sub)
    markup.add(nft, ido, airdrop, free)

    user_status = bot.get_chat_member(chat_id='-1001705740568', user_id=call.message.chat.id)

    sti = open('static1/pic/welocome.png', 'rb')

    if call.data == 'like':
        if user_status.status == 'member' or user_status.status == 'creator' or user_status.status == 'administrator':
            bot.send_photo(call.message.chat.id, sti)
            bot.send_message(call.message.chat.id,
                             "Привет, {0.first_name}!👋\nЯ - {1.first_name}, меня создали, чтобы я напоминал о важных событиях в крипто-мире.🌎".format(
                                 call.message.chat, bot.get_me()), parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, "😔 Вы ещё не подписались на наш канал.\n",parse_mode='html', reply_markup=markup2)


@bot.message_handler(commands=['special'])
def mess(message):
    if str(message.chat.id) not in admins:
        return
    notif = open("static1/Notif/all_notif.txt", "rb").read()
    all_users = open("static1/Notif_id/rasslika.txt", "r")
    for line in all_users.readlines():
        joinedUsers.add(line.strip())
    print("spec")
    print(joinedUsers)
    for user in joinedUsers:
        bot.send_message(user, notif, disable_web_page_preview=True)

@bot.message_handler(commands=['nft_notif'])
def nft_mess(message):
    if str(message.chat.id) not in admins:
        return
    nft_notif = open("static1/Notif/nft_notif.txt", "rb").read()
    nft_users = open("static1/Notif_id/nft_id.txt", "r")
    for line in nft_users.readlines():
        Subnft.add(line.strip())
    print("nft_notif")
    print(Subnft)
    for user in Subnft:
        bot.send_message(user, nft_notif, disable_web_page_preview=True)

@bot.message_handler(commands=['ido_notif'])
def nft_mess(message):
    if str(message.chat.id) not in admins:
        return
    ido_notif = open("static1/Notif/ido_notif.txt", "rb").read()
    ido_users = open("static1/Notif_id/ido_id.txt", "r")
    for line in ido_users.readlines():
        Subido.add(line.strip())
    print("ido_notif")
    print(Subido)
    for user in Subido:
        bot.send_message(user, ido_notif, disable_web_page_preview=True)

@bot.message_handler(commands=['freenft_notif'])
def mess(message):
    if str(message.chat.id) not in admins:
        return
    freenft_notif = open("static1/Notif/freenft_notif.txt", "rb").read()
    freenft_users = open("static1/Notif_id/freenft_id.txt", "r")
    for line in freenft_users.readlines():
        Subfree_nft.add(line.strip())
    print("free nft notif")
    print(Subfree_nft)
    for user in joinedUsers:
        bot.send_message(user, freenft_notif, disable_web_page_preview=True)

@bot.message_handler(commands=['airdrop_notif'])
def mess(message):
    if str(message.chat.id) not in admins:
        return
    airdrop_notif = open("static1/Notif/airdrop_notif.txt", "rb").read()
    airdrop_users = open("static1/Notif_id/airdrop_id.txt", "r")
    for line in airdrop_users.readlines():
        Subairdrop.add(line.strip())
    print("airdrop notif")
    print(Subairdrop)
    for user in joinedUsers:
        bot.send_message(user, airdrop_notif, disable_web_page_preview=True)


@bot.message_handler(content_types=['text'])
def lalala(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    back = types.KeyboardButton("◀️ Назад")

    #кнопки NFT
    nft = types.KeyboardButton("🖼 NFT")
    nft_notif = types.KeyboardButton("🔔 Получать обновления по NFT")
    nft_unnotif = types.KeyboardButton("🔕 Не получать обновления по NFT")

    #кнопки IDO
    ido = types.KeyboardButton("🪙 TokenSale")
    ido_notif = types.KeyboardButton("🔔 Получать обновления по TokenSale")
    ido_unnotif = types.KeyboardButton("🔕 Не получать обновления по TokenSale")

    #кнопки Airdrop
    airdrop = types.KeyboardButton("🚀 AirDrop")
    airdrop_notif = types.KeyboardButton("🔔 Получать обновления по Airdrop")
    airdrop_unnotif = types.KeyboardButton("🔕 Не получать обновления по Airdrop")

    #кнопки FreeNFT
    free = types.KeyboardButton("🆓 Free NFT")
    freenft_notif = types.KeyboardButton("🔔 Получать обновления по Free NFT")
    freenft_unnotif = types.KeyboardButton("🔕 Не получать обновления по Free NFT")


    if message.text == '🪙 TokenSale':
            idotxt = open('static1/post/ido.txt', 'rb').read()
            idopic = open('static1/pic/tokensale.png', 'rb')
            if str(message.chat.id) not in Subido:
                bot.send_photo(message.chat.id, idopic)
                bot.send_message(message.chat.id, idotxt, reply_markup=markup.add(back, ido_notif), disable_web_page_preview=True)
            elif str(message.chat.id) in Subido:
                bot.send_photo(message.chat.id, idopic)
                bot.send_message(message.chat.id, idotxt, reply_markup=markup.add(back, ido_unnotif), disable_web_page_preview=True)

    elif message.text == '🖼 NFT':
            nfttxt = open('static1/post/nft.txt', 'rb').read()
            nftpic = open('static1/pic/nft.png', 'rb')
            if str(message.chat.id) not in Subnft:
                bot.send_photo(message.chat.id, nftpic)
                bot.send_message(message.chat.id, nfttxt, reply_markup=markup.add(back, nft_notif), disable_web_page_preview=True)
            elif str(message.chat.id) in Subnft:
                bot.send_photo(message.chat.id, nftpic)
                bot.send_message(message.chat.id, nfttxt, reply_markup=markup.add(back, nft_unnotif), disable_web_page_preview=True)

    elif message.text == '🚀 AirDrop':
            airdroptxt = open('static1/post/airdrop.txt', 'rb').read()
            airdroppic = open('static1/pic/airdrop.png', 'rb')
            if str(message.chat.id) not in Subairdrop:
                bot.send_photo(message.chat.id, airdroppic)
                bot.send_message(message.chat.id, airdroptxt, reply_markup=markup.add(back, airdrop_notif), disable_web_page_preview=True)
            elif str(message.chat.id) in Subairdrop:
                bot.send_message(message.chat.id, airdroptxt, reply_markup=markup.add(back, airdrop_unnotif), disable_web_page_preview=True)

    elif message.text == '🆓 Free NFT':
            freenfttxt = open('static1/post/freenft.txt', 'rb').read()
            freenftpic = open('static1/pic/freenft.png', 'rb')
            if str(message.chat.id) not in Subfree_nft:
                bot.send_photo(message.chat.id, freenftpic)
                bot.send_message(message.chat.id, freenfttxt, reply_markup=markup.add(back, freenft_notif), disable_web_page_preview=True)
            elif str(message.chat.id) in Subfree_nft:
                bot.send_message(message.chat.id, freenfttxt, reply_markup=markup.add(back, freenft_unnotif), disable_web_page_preview=True)

    elif message.text == '◀️ Назад':
            bot.send_message(message.chat.id, "Выберите то, что вас интересует", reply_markup=markup.add( nft, ido, airdrop, free))



    #подписка на NFT
    if message.text == "🔔 Получать обновления по NFT":
        nft_sub_file = open("static1/Notif_id/nft_id.txt", "r")
        for line in nft_sub_file.readlines():
            Subnft.add(line.strip())
        nft_sub_file.close()
        print("sub to nft")
        if not str(message.chat.id) in Subnft:
            nft_sub_file = open("static1/Notif_id/nft_id.txt", "a")
            nft_sub_file.write(str(message.chat.id) + "\n")
            Subnft.add(str(message.chat.id))
        bot.send_message(message.chat.id, "Вы подписались на обновления по NFT", reply_markup=markup.add(back, nft_unnotif))

    # отписка от NFT
    if message.text == "🔕 Не получать обновления по NFT":
        nft_sub_file = open("static1/Notif_id/nft_id.txt", "a")
        nft_sub_file.truncate(0)
        print("unsub to nft")
        Subnft.remove(str(message.chat.id))
        for user in Subnft:
            nft_sub_file.write(user + '\n')
        bot.send_message(message.chat.id, "Вы отменили подписку на обновления по NFT", reply_markup=markup.add(back,nft_notif))



    # подписка на FREE NFT
    if message.text == "🔔 Получать обновления по Free NFT":
        freenft_sub_file = open("static1/Notif_id/freenft_id.txt", "r")
        for line in freenft_sub_file.readlines():
            Subfree_nft.add(line.strip())
        freenft_sub_file.close()
        print("sub to freenft")
        if not str(message.chat.id) in Subfree_nft:
            freenft_sub_file = open("static1/Notif_id/freenft_id.txt", "a")
            freenft_sub_file.write(str(message.chat.id) + "\n")
            Subfree_nft.add(str(message.chat.id))
        bot.send_message(message.chat.id, "Вы подписались на обновления по FREE NFT", reply_markup=markup.add(back, freenft_unnotif))

    # отписка от FREE NFT
    if message.text == "🔕 Не получать обновления по Free NFT":
        freenft_sub_file = open("static1/Notif_id/freenft_id.txt", "a")
        freenft_sub_file.truncate(0)
        print("unsub to nft")
        Subfree_nft.remove(str(message.chat.id))
        for user in Subfree_nft:
            freenft_sub_file.write(user + '\n')
        bot.send_message(message.chat.id, "Вы отменили подписку на обновления по FREE NFT", reply_markup=markup.add(back, freenft_notif))



    # подписка на IDO
    if message.text == "🔔 Получать обновления по TokenSale":
        ido_sub_file = open("static1/Notif_id/ido_id.txt", "r")
        for line in ido_sub_file.readlines():
            Subido.add(line.strip())
        ido_sub_file.close()
        print("sub to ido")
        if not str(message.chat.id) in Subido:
            ido_sub_file = open("static1/Notif_id/ido_id.txt", "a")
            ido_sub_file.write(str(message.chat.id) + "\n")
            Subido.add(str(message.chat.id))
        bot.send_message(message.chat.id, "Вы подписались на обновления по TokenSale", reply_markup=markup.add(back, ido_unnotif))

    # отписка от IDO
    if message.text == "🔕 Не получать обновления по TokenSale":
        ido_sub_file = open("static1/Notif_id/ido_id.txt", "a")
        ido_sub_file.truncate(0)
        print("unsub to ido")
        Subido.remove(str(message.chat.id))
        for user in Subido:
            ido_sub_file.write(user + '\n')
        bot.send_message(message.chat.id, "Вы отменили подписку на обновления по TokenSale", reply_markup=markup.add(back, ido_notif))



    # подписка на Airdrop
    if message.text == "🔔 Получать обновления по Airdrop":
        airdrop_sub_file = open("static1/Notif_id/airdrop_id.txt", "r")
        for line in airdrop_sub_file.readlines():
            Subairdrop.add(line.strip())
        airdrop_sub_file.close()
        print("sub to airdrop")
        if not str(message.chat.id) in Subairdrop:
            airdrop_sub_file = open("static1/Notif_id/airdrop_id.txt", "a")
            airdrop_sub_file.write(str(message.chat.id) + "\n")
            Subairdrop.add(str(message.chat.id))
        bot.send_message(message.chat.id, "Вы подписались на обновления по Airdrop", reply_markup=markup.add(back, airdrop_unnotif))

    # отписка от IDO
    if message.text == "🔕 Не получать обновления по Airdrop":
        airdrop_sub_file = open("static1/Notif_id/airdrop_id.txt", "a")
        airdrop_sub_file.truncate(0)
        print("unsub to airdrop")
        Subairdrop.remove(str(message.chat.id))
        for user in Subairdrop:
            airdrop_sub_file.write(user + '\n')
        bot.send_message(message.chat.id, "Вы отменили подписку на обновления по Airdrop", reply_markup=markup.add(back, airdrop_notif))


bot.polling(none_stop=True)
