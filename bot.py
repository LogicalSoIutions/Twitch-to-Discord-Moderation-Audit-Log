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

# Connect to Twitch PubSub
ws = websocket.WebSocket()
ws.connect(endpoint)

# Subscribe to channel point redemption topic
subscribe_message = {
    "type": "LISTEN",
    "data": {"topics": [redemption_topic], "auth_token": token},
}
ws.send(json.dumps(subscribe_message))

# Heartbeat function to send PING messages to Twitch at regular intervals
def send_heartbeat():
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
        "description": f"`{data['data']['created_by']}` used command `/delete {msgArgs}` at your local time of: <t:{epoch_seconds}>\n\n[View usercard for {data['data']['args'][0]}](https://twitch.tv/popout/lvndmark/viewercard/{data['data']['args'][0]})",
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
        "description": f"`{data['data']['created_by']}` used command `/timeout {msgArgs}` at your local time of: <t:{epoch_seconds}>\n\n[View usercard for {data['data']['args'][0]}](https://twitch.tv/popout/lvndmark/viewercard/{data['data']['args'][0]})",
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
        "description": f"`{data['data']['created_by']}` used command `/ban {msgArgs}` at your local time of: <t:{epoch_seconds}>\n\n[View usercard for {data['data']['args'][0]}](https://twitch.tv/popout/lvndmark/viewercard/{data['data']['args'][0]})",
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
        "description": f"`{data['data']['created_by']}` used command `/unban {msgArgs}` at your local time of: <t:{epoch_seconds}>",
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
        "description": f"`{data['data']['created_by']}` used command `/untimeout {msgArgs}` at your local time of: <t:{epoch_seconds}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_slowmode(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/slow {data['data']['args'][0]}` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_emotemode(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/emoteonly` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    print(embed)
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_submode(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/subscribers` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_followmode(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/followers {data['data']['args'][0]}` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def enable_r9k(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/r9kbeta` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_slowmode(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/slowoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_emotemode(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/emoteonlyoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_submode(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/subscribersoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_followmode(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/followersoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


def disable_r9k(data, webhook_url):
    embed = {
        "description": f"`{data['data']['created_by']}` used command `/r9kbetaoff` at your local time of: <t:{int(time.time())}>",
        "color": generate_hex_code(),
    }
    payload = {"embeds": [embed]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()


# Create and start heartbeat thread
heartbeat_thread = threading.Thread(target=send_heartbeat)
heartbeat_thread.start()

# Listen for messages from Twitch PubSub
while True:
    try:
        message = ws.recv()
    except websocket.WebSocketConnectionClosedException:
        # Handle connection loss by reconnecting and resubscribing
        ws.close()
        ws.connect(endpoint)
        ws.send(json.dumps(subscribe_message))
        continue
    except KeyboardInterrupt:
        print("Closed via CTRL + C")
        sys.exit()
    message = json.loads(message)

    if message["type"] == "RECONNECT":
        # Reconnect if Twitch requests it
        ws.close()
        ws.connect(endpoint)
        ws.send(json.dumps(subscribe_message))
    elif message["type"] == "MESSAGE":
        data = json.loads(message["data"]["message"])
        moderation_action = data["data"]["moderation_action"]

        if moderation_action == "delete":
            delete_message(data, webhook_url)
        elif moderation_action == "timeout":
            timeout_message(data, webhook_url)
        elif moderation_action == "slow":
            enable_slowmode(data, webhook_url)
        elif moderation_action == "emoteonly":
            enable_emotemode(data, webhook_url)
        elif moderation_action == "subscribers":
            enable_submode(data, webhook_url)
        elif moderation_action == "followers":
            enable_followmode(data, webhook_url)
        elif moderation_action == "r9kbeta":
            enable_r9k(data, webhook_url)
        elif moderation_action == "slowoff":
            disable_slowmode(data, webhook_url)
        elif moderation_action == "emoteonlyoff":
            disable_emotemode(data, webhook_url)
        elif moderation_action == "subscribersoff":
            disable_submode(data, webhook_url)
        elif moderation_action == "followersoff":
            disable_followmode(data, webhook_url)
        elif moderation_action == "r9kbetaoff":
            disable_r9k(data, webhook_url)
        elif moderation_action == "ban":
            ban_message(data, webhook_url)
        elif moderation_action == "unban":
            unban_message(data, webhook_url)
        elif moderation_action == "untimeout":
            untimeout_message(data, webhook_url)
        else:
            print(data)
    else:
        print(message)
