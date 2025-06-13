from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_to_slack(channel: str, message: str, slack_token: str):
    client = WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(channel=channel, text=message[:3000])
        print(f"[SUCCESS] Message sent to Slack channel {channel}")
    except SlackApiError as e:
        print(f"[ERROR] Slack API: {e.response['error']}")