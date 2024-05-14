"""receiver from Telegram chat"""

import time

import asyncio
from telethon import TelegramClient, events
from telethon.types import UpdateShortMessage, UpdateNewChannelMessage, UpdateNewMessage

from core.config import project_settings

client = TelegramClient("anon", project_settings.api_id, project_settings.api_hash)


@client.on(events.NewMessage())
async def receiver(event):
    """Return Sender, name of channel (if exist), message in receiver mode
    without attachments (photos, videos, files, etc)
    """
    sender = await event.get_sender()

    if isinstance(event.original_update, (UpdateShortMessage, UpdateNewMessage)):
        channel = None
        message = event.message.message
    if isinstance(event.original_update, UpdateNewChannelMessage):
        channel = await client.get_entity(event.message.peer_id)
        message = event.message.message

    if channel:
        print(f"From {sender.username} in channel {channel.title}\n\n{message} \n")
    else:
        print(f"From {sender.username} \n\n{message}\n")


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
