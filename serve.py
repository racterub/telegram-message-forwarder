#!/usr/bin/env python3

# Author: Racter Liu (Racterub / root@racterub.me)

from config import TOKEN, BOT_CHAT_ID, USERNAME
from telegram.ext import Updater, Filters, MessageHandler


def file_handler(update, context):
    """File handler for fowarding images and files to BOT_CHAT_ID
    Ref: https://stackoverflow.com/questions/65882704/how-to-forward-image-to-another-chat-with-telegram-bot-python-api
    Args:
        update (Object): Update
        context (Object): Context
    """
    if update.message['photo'] == []:
        # File
        fileID = update.message['document']['file_id']
        fileName = update.message['document']['file_name']
        caption = update.message['caption']
        context.bot.sendDocument(
            chat_id = BOT_CHAT_ID,
            filename = fileName,
            caption = caption,
            document = fileID
        )
    else:
        # Image
        fileID = update.message['photo'][-1]['file_id']
        caption = update.message['caption']
        context.bot.sendPhoto(
        chat_id = BOT_CHAT_ID,
        caption = caption,
        photo = fileID
    )

def message_handler(update, context):
    context.bot.sendMessage(
        chat_id=BOT_CHAT_ID,
        text=f"{update.message.text}"
    )


if __name__=='__main__':
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    #Add Image/File handler
    dispatcher.add_handler(
        MessageHandler(
            (Filters.document | Filters.photo) & Filters.user(username=f"@{USERNAME}"),
        file_handler
        )
    )
    #Add Message handler
    dispatcher.add_handler(
        MessageHandler(
            (Filters.text | (~Filters.command)) & Filters.user(username=f"@{USERNAME}"),
            message_handler
        )
    )

    updater.start_polling()
