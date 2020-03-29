from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)

from modules.Response import Response

app = Flask(__name__)


line_bot_api = LineBotApi('b0cby3MIWx8TGKNnSW8cL46GtT9hPP9QR+gvxJ0bAVVbvODsY12bjrluRaZaVHA0us+ouu8/EvnB11lNZfP8v59bywJ0xIuvDe7d1Q+G+ntbkvvyM7nAsNvgGTWruSBuPTG61/H7Fzn+6hQOCYsy5AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('463aeafd79d78ccb50e96d758190b283')

@app.route("/")
def hello():
    return "hello world!!"

@app.route("/webhook", methods=['POST'])
def webhook():

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # User information
    user_msg = event.message.text
    profile = line_bot_api.get_profile(event.source.user_id)

    # Define Response object
    msg_handler = Response(user_msg, profile)

    # Reply
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg_handler.conversation()))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')