"""receiver from Telegram chat"""

import asyncio
import argparse
import time

from telethon import TelegramClient, events

from core.config import project_settings

parser = argparse.ArgumentParser()
parser.add_argument("--chat", "-c", help="Chat name, e.g., rian_ru")

args = parser.parse_args()

client = TelegramClient("anon", project_settings.api_id, project_settings.api_hash)


@client.on(events.NewMessage(chats=args.chat))
async def text_receiver(event):
    """Return raw text from chat without attachments"""
    print(event.raw_text)


async def main():
    """main loop"""

    while True:
        try:
            await asyncio.sleep(10)
        except (ConnectionError, TimeoutError):
            time.sleep(10)


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
