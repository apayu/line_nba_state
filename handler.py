import os
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


def webhook(event, context):
    line_bot_api = LineBotApi(os.environ['LINE_ACCESS_TOKEN'])
    handler = WebhookHandler(os.environ['LINE_SECRET'])

    msg = json.loads(event['body'])
    line_bot_api.reply_message(
        msg['events'][0]['replyToken'],
        TextSendMessage(text=msg['events'][0]['message']['text'])
    )
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": 'ok'})
    }

    return response
