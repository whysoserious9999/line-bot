# SDK software development kit
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('8NvL/sNdhaODfdpgqtMbmGPwBDcdZ8K0buE0BAINOZpFhtnHo7qEQr1RxDEpJ9390uuLVrcJqSmbIqpaFA+voI8IbZ7S2kiqcZoHxzrYIptLI/28vBJFf2ICSo9MQlAzNoFysZ7tEBlykw71L85HjwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0482d4c32411d60ae811e2100b02b535')


@app.route("/callback", methods=['POST'])
def callback():
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
	#line_bot_api.reply_message(
    #    event.reply_token,
    #    TextSendMessage(text='輸入start>>開啟對話/輸入end>>結束對話'))

	msg = event.message.text
	if msg == 'start':
		reply='你好,請輸入你的姓名'
	elif msg == 'end':
		reply='謝謝您使用本功能'
	else:
		reply='請重新輸入,謝謝'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()