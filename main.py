# from fastapi import FastAPI
import os
from slack import RTMClient
from slack.errors import SlackApiError

BOT_NAME = 'myslackbot'
SLACK_API_TOKEN = "RMm19mCPsKfNiEMwsjirkXhN"

@RTMClient.run_on(event='team_join')
def message_to_new_user(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    user = data['user']
    print("================")
    print(user)
    print("================")
    try:
        response = webclient.chat_postMessage(
            text=f"Useful Resources",
            as_user=true
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"] # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
rtm_client = RTMClient(token=SLACK_API_TOKEN)
rtm_client.start()


# app = FastAPI()

# @app.get("/")
# def home():
#     return {"Hello", "World"}