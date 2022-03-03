from base64 import b64decode
from itertools import cycle
from websocket import WebSocketApp
import json


class Monitor:

    def __init__(self, api_key, decrypt_key, scopes, notification_handler):
        self.decrypt_key = decrypt_key
        self.notification_handler = notification_handler

        self.headers = [
            f'Authorization: {api_key}',
            f'scopes: [{",".join(scopes)}]',
        ]

    def on_message(ws, s, message):
        ws.notification_handler(ws.decrypt(message, ws.decrypt_key))

    def on_error(ws, s, error):
        print("errror:", error)

    def on_close(ws, close_status_code, close_msg, s):
        print("### closed ###")

    def on_open(ws, s):
        print("Opened connection")

    def decrypt(self, data, key):
        return json.loads(''.join(chr(ord(a) ^ ord(b)) for a, b in zip(b64decode(data).decode("utf-8"), cycle(key))))

    def connect(self):
        ws = WebSocketApp("ws://api.bullseye.pw/v1/ws/",
                          on_open=self.on_open,
                          on_message=self.on_message,
                          on_error=self.on_error,
                          on_close=self.on_close,
                          header=self.headers)
        ws.run_forever()
