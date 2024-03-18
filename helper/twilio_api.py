import os


from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


account_sid = 'AC02723908f4f5666c9e9975fc1f835a2b'
auth_token = '93d58dca8ea0e0855ca9a374a56ed6a7'
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
    

    _ = client.messages.create(from_='whatsapp:+14155238886',body=message,to=to)
