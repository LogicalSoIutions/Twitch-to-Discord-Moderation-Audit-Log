import websocket
import json
import time
import requests
import threading
import random
import sys
from dateutil import parser

# Twitch PubSub endpoint
endpoint = "wss://pubsub-edge.twitch.tv"

# Your Twitch OAuth token
token = "yourTwitchOAuthToken"

# Twitch channel ID and redemption topic
redemption_topic = "chat_moderator_actions.yourUserID.channelModeratingUserID"

# Define the webhook URL and the message content
webhook_url = 'yourDiscordWebhookURLhere'

# Heartbeat interval in seconds
heartbeat_interval = 280

# Heartbeat function to send PING messages to Twitch at regular intervals
def send_heartbeat(ws):
    while True:
        ws.send(json.dumps({"type": "PING"}))
        print("PING")
        time.sleep(heartbeat_interval)


def generate_hex_code():
    color = random.randint(0, 16777215)
    return color


def delete_message(data, webhook_url):
    msgArgs = data["data"]["args"][0] + " " + data["data"]["args"][1]
    dt_obj = parser.parse(data["data"]["created_at"])
    epoch_seconds = int(dt_obj.timestamp())
    embed = {
        "title": f"**Message Deleted** by **{data['data']['created_by']}**",
        "description": f"Command used `/delete {msgArgs}` at your local time of: <t:{epoch_seconds}>\n\n[View usercard for {data['data']['args'][0]}](https://twitch.tv/popout/lvndmark/viewercard/{data['data']['args'][0]})",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def timeout_message(data, webhook_url):
    msgArgs = data["data"]["args"][0] + " " + data["data"]["args"][1]
    dt_obj = parser.parse(data["data"]["created_at"])
    epoch_seconds = int(dt_obj.timestamp())
    embed = {
        "title": f"**User Timedout** by **{data['data']['created_by']}**",
        "description": f"Command used`/timeout {msgArgs}` at your local time of: <t:{epoch_seconds}>\n\n[View usercard for {data['data']['args'][0]}](https://twitch.tv/popout/lvndmark/viewercard/{data['data']['args'][0]})",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def ban_message(data, webhook_url):
    msgArgs = data["data"]["args"][0] + " " + data["data"]["args"][1]
    dt_obj = parser.parse(data["data"]["created_at"])
    epoch_seconds = int(dt_obj.timestamp())
    embed = {
        "title": f"**User Banned** by **{data['data']['created_by']}**",
        "description": f"Command used`/ban {msgArgs}` at your local time of: <t:{epoch_seconds}>\n\n[View usercard for {data['data']['args'][0]}](https://twitch.tv/popout/lvndmark/viewercard/{data['data']['args'][0]})",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def unban_message(data, webhook_url):
    msgArgs = data["data"]["args"][0]
    dt_obj = parser.parse(data["data"]["created_at"])
    epoch_seconds = int(dt_obj.timestamp())
    embed = {
        "title": f"**User Unbanned** by **{data['data']['created_by']}**",
        "description": f"Command used`/unban {msgArgs}` at your local time of: <t:{epoch_seconds}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def untimeout_message(data, webhook_url):
    msgArgs = data["data"]["args"][0]
    dt_obj = parser.parse(data["data"]["created_at"])
    epoch_seconds = int(dt_obj.timestamp())
    embed = {
        "title": f"**Timeout Removed** by **{data['data']['created_by']}**",
        "description": f"Command used`/untimeout {msgArgs}` at your local time of: <t:{epoch_seconds}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_slowmode(data, webhook_url):
    embed = {
        "title": f"**Slow Mode Enabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/slow {data['data']['args'][0]}` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_emotemode(data, webhook_url):
    embed = {
        "title": f"**Emote Only Mode Enabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/emoteonly` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    print(embed)
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_submode(data, webhook_url):
    embed = {
        "title": f"**Sub Only Mode Enabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/subscribers` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_followmode(data, webhook_url):
    embed = {
        "title": f"**Follower Only Mode Enabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/followers {data['data']['args'][0]}` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_r9k(data, webhook_url):
    embed = {
        "title": f"**R9K Mode Enabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/r9kbeta` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_slowmode(data, webhook_url):
    embed = {
        "title": f"**Slow Mode Disabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/slowoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_emotemode(data, webhook_url):
    embed = {
        "title": f"**Emote Only Mode Disabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/emoteonlyoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_submode(data, webhook_url):
    embed = {
        "title": f"**Sub Only Mode Disabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/subscribersoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_followmode(data, webhook_url):
    embed = {
        "title": f"**Follower Only Mode Disabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/followersoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_r9k(data, webhook_url):
    embed = {
        "title": f"**R9K Mode Disabled** by **{data['data']['created_by']}**",
        "description": f"Command used`/r9kbetaoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()

subscribe_message = {
            "type": "LISTEN",
            "data": {"topics": [redemption_topic], "auth_token": token},
        }

def listen_for_messages(ws, webhook_url):
    while True:
        try:
            message = ws.recv()
        except websocket.WebSocketConnectionClosedException:
            ws.connect(endpoint)
            ws.send(json.dumps(subscribe_message))
            continue
        except KeyboardInterrupt:
            print("Closed via CTRL + C")
            sys.exit()
        message = json.loads(message)

        if message["type"] == "RECONNECT":
            ws.connect(endpoint)
            ws.send(json.dumps(subscribe_message))
        elif message["type"] == "MESSAGE":
            data = json.loads(message["data"]["message"])
            moderation_action = data["data"]["moderation_action"]

            action_functions = {
                "delete": delete_message,
                "timeout": timeout_message,
                "slow": enable_slowmode,
                "emoteonly": enable_emotemode,
                "subscribers": enable_submode,
                "followers": enable_followmode,
                "r9kbeta": enable_r9k,
                "slowoff": disable_slowmode,
                "emoteonlyoff": disable_emotemode,
                "subscribersoff": disable_submode,
                "followersoff": disable_followmode,
                "r9kbetaoff": disable_r9k,
                "ban": ban_message,
                "unban": unban_message,
                "untimeout": untimeout_message,
            }

            if moderation_action in action_functions:
                action_functions[moderation_action](data, webhook_url)
            else:
                print(data)
        else:
            print(message)

def main():
    # Connect to Twitch PubSub
        ws = websocket.WebSocket()
        ws.connect(endpoint)
        # Subscribe to channel point redemption topic
        subscribe_message = {
            "type": "LISTEN",
            "data": {"topics": [redemption_topic], "auth_token": token},
        }
        ws.send(json.dumps(subscribe_message))

        # Create and start heartbeat thread
        heartbeat_thread = threading.Thread(target=send_heartbeat, args=(ws,))
        heartbeat_thread.start()

        # Listen for messages from Twitch PubSub
        listen_for_messages(ws, webhook_url)

if __name__ == "__main__":
    main()
